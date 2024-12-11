# utils.py
import os
import requests
import pandas as pd
from lxml import etree

NAMESPACES = {
    "clin_shared": "http://tcga.nci/bcr/xml/clinical/shared/2.7",
    "shared": "http://tcga.nci/bcr/xml/shared/2.7",
}

GDC_API_URL = "https://api.gdc.cancer.gov/data/"

def get_gdc_file_ids(project_id="TCGA-UCEC", data_type="Clinical Supplement"):
    """
    Retrieve GDC file IDs for a given project and data type.
    """
    GDC_FILES_URL = "https://api.gdc.cancer.gov/files"
    params = {
        "filters": {
            "op": "and",
            "content": [
                {"op": "in", "content": {"field": "cases.project.project_id", "value": [project_id]}},
                {"op": "in", "content": {"field": "data_category", "value": ["Clinical"]}},
                {"op": "in", "content": {"field": "data_type", "value": [data_type]}}
            ]
        },
        "format": "JSON",
        "size": 1000
    }

    response = requests.post(GDC_FILES_URL, json=params)
    if response.status_code == 200:
        file_data = response.json()["data"]["hits"]
        file_ids = [file["file_id"] for file in file_data]
        return file_ids
    else:
        raise Exception(f"Failed to retrieve file IDs. Status code: {response.status_code}")

def download_xml_files(file_ids, output_dir):
    """
    Download XML files from the GDC Data Portal using file IDs.
    """
    os.makedirs(output_dir, exist_ok=True)
    for file_id in file_ids[100:]:
        print(f"Downloading file ID: {file_id}")
        try:
            response = requests.get(GDC_API_URL + file_id, stream=True)
            if response.status_code == 200:
                content_disposition = response.headers.get("Content-Disposition", "")
                file_name = content_disposition.split("filename=")[-1].strip('"') if "filename=" in content_disposition else f"{file_id}.xml"
                file_path = os.path.join(output_dir, file_name)
                with open(file_path, "wb") as f:
                    for chunk in response.iter_content(chunk_size=8192):
                        f.write(chunk)
                print(f"Downloaded: {file_name}")
            else:
                print(f"Failed to download file ID: {file_id}. Status code: {response.status_code}")
        except Exception as e:
            print(f"Failed to download file ID: {file_id}. Error: {e}")

            
def extract_race_from_xml(xml_file):
    """
    Extract race information from a single XML file.
    """
    tree = etree.parse(xml_file)
    root = tree.getroot()

    race_data = {}
    for race_elem in root.findall(".//clin_shared:race_list/clin_shared:race", NAMESPACES):
        race = race_elem.text
        parent = race_elem.getparent().getparent()  # Move up to the patient level
        patient_id_elem = parent.find("shared:bcr_patient_barcode", NAMESPACES)
        if patient_id_elem is not None:
            patient_id = patient_id_elem.text
            race_data[f"{patient_id}"] = race 
    
    return race_data

def extract_ethnicity_from_xml(xml_file):
    """
    Extract ethnicity information from a single XML file.
    """
    tree = etree.parse(xml_file)
    root = tree.getroot()  # Corrected: Use getroot()

    ethnicity_data = {}
    # Confirm and adjust the XPath for ethnicity if needed
    for ethnicity_elem in root.findall(".//clin_shared:ethnicity", NAMESPACES):
        ethnicity = ethnicity_elem.text
        # Get the parent element to navigate to patient ID
        parent = ethnicity_elem.getparent().getparent()  # Move up to the patient level
        patient_id_elem = parent.find(".//shared:bcr_patient_barcode", NAMESPACES)
        if patient_id_elem is not None:
            patient_id = patient_id_elem.text
            ethnicity_data[f"{patient_id}"] = ethnicity  # Ensure correct patient ID format

    return ethnicity_data

def load_race_data(xml_dir):
    """
    Load race data from XML files and filter for relevant samples.
    """
    race_dict = {}
    for xml_file in os.listdir(xml_dir):
        if xml_file.endswith(".xml") and xml_file.startswith("nationwidechildrens.org_clinical.TCGA-"):
            full_path = os.path.join(xml_dir, xml_file)
            race_dict.update(extract_race_from_xml(full_path))
    
    return pd.DataFrame(list(race_dict.items()), columns=["sample", "race"])

def load_ethnicity_data(xml_dir):
    """
    Load ethnicity data from multiple XML files.

    Parameters:
    - xml_dir (str): Directory containing XML files.

    Returns:
    - DataFrame: DataFrame with patient IDs and ethnicity.
    """
    ethnicity_dict = {}
    for xml_file in os.listdir(xml_dir):
        if xml_file.endswith(".xml") and xml_file.startswith("nationwidechildrens.org_clinical.TCGA-"):
            full_path = os.path.join(xml_dir, xml_file)
            ethnicity_dict.update(extract_ethnicity_from_xml(full_path))
    
    return pd.DataFrame(list(ethnicity_dict.items()), columns=["sample", "ethnicity"])


def load_expression_data(expression_file, samples, genes_of_interest, temp_file="filtered_expression_data.txt"):
    """
    Load expression data and filter for relevant samples and genes.

    Parameters:
    - expression_file (str): Path to the expression data file.
    - samples (list): List of sample IDs to include.
    - genes_of_interest (list): List of gene names to include.
    - temp_file (str): Temporary file to store filtered expression data.

    Returns:
    - DataFrame: Expression data filtered for the given samples and genes.
    """
    print("Filtering expression data...")

    # Read the header to find matching sample columns
    with open(expression_file, "r") as f:
        header = f.readline().strip().split('\t')
        # remove the "-01" at the end of each header
        
    # Determine which columns to keep
    columns_to_keep = [0] + [i for i, col in enumerate(header) if col in samples]

    if len(columns_to_keep) <= 1:
        print("No matching samples found in the header.")
        raise ValueError("No matching samples found in expression data.")

    # Write filtered data to a temporary file
    with open(temp_file, "w") as out_f:
        # Write the header
        out_f.write('\t'.join([header[i][0:-3] for i in columns_to_keep]) + '\n')

        # Filter rows based on genes of interest
        for line in open(expression_file, "r"):
            split_line = line.strip().split('\t')
            gene_name = split_line[0]  # First column contains the gene names
            if gene_name in genes_of_interest:
                out_f.write('\t'.join([split_line[i] for i in columns_to_keep]) + '\n')

    # Load the filtered data into a DataFrame
    print("Loading filtered data into DataFrame...")
    expr_df = pd.read_csv(temp_file, sep='\t',header=0, encoding='latin1')

    # Return the filtered DataFrame
    return expr_df