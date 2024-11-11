import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
from sklearn.metrics import roc_auc_score
import numpy as np
import io, sys, os, requests, subprocess, html2text

DISCOTOPE_FOLDER = '/home/leandro/DiscoTope-3.0'
EXPRESSION_FILE = 'data/uterus_exp_data.txt'
PHENOTYPES_FILE = 'data/uterus_exp_phenotypes.txt'

def run_discotope(uniprot_accession, save_to=None):
    """
    Run Discotope on a given Uniprot accession.
    """

    # TODO: this shouldn't be hardcoded
    env_path = f'{DISCOTOPE_FOLDER}/discotope/bin/activate'

    # Script you want to run in the called environment
    pdb_path = f'/data/alphafold/{uniprot_accession[1:3]}/{uniprot_accession}.pdb'
    script_path = f'{DISCOTOPE_FOLDER}/discotope3/main.py --pdb_or_zip_file {pdb_path} --struc_type alphafold --out_dir {save_to} --cpu_only'

    command = f"cd {DISCOTOPE_FOLDER} && source {env_path} && python {script_path}"

    # Run the script using the called environment's Python interpreter
    subprocess.run(command, shell=True, executable='/bin/bash')

def compare_gene_expression(gene_name, up_acc, save_to=None):
    """
    Compare expression levels of a specified gene between normal uterus tissue and uterine carcinosarcoma samples.
    """
    # Read the expression data
    expr_df = pd.read_csv(EXPRESSION_FILE, sep='\t', encoding='latin1')
    phenotype_df = pd.read_csv(PHENOTYPES_FILE, sep='\t', header=None, encoding='latin1')
    
    # Transpose the DataFrame to have samples as rows and genes as columns
    expr_df.set_index('sample', inplace=True)
    expr_df = expr_df.transpose().reset_index()
    expr_df.rename(columns={'index': 'sample'}, inplace=True)
    
    # Check if the gene exists in the expression data
    if gene_name not in expr_df.columns:
        print(f"Gene '{gene_name}' not found in the expression data.")
        return
    
    phenotype_df.columns = ['sample', 'primary_disease', 'disease', 'primary_site', 'sample_type', 'gender', 'project_id']
    
    # Merge the expression data with phenotype data
    merged_df = pd.merge(expr_df[['sample', gene_name]], phenotype_df, on='sample', how='left')
    
    # Filter samples to include only 'Normal Tissue' and 'Uterine Carcinosarcoma'
    # Filter for normal uterus samples
    normal_samples = merged_df[
        (merged_df['sample_type'] == 'Normal Tissue') &
        (merged_df['primary_site'] == 'Uterus')
    ]

    # Filter for uterine carcinosarcoma samples
    cancer_samples = merged_df[
        merged_df['primary_disease'] == 'Uterine Corpus Endometrioid Carcinoma'
    ]

    # Extract the expression values for the specified gene
    normal_expression = normal_samples[gene_name].dropna()
    cancer_expression = cancer_samples[gene_name].dropna()
    normal_expression_mean = normal_expression.mean()
    cancer_expression_mean = cancer_expression.mean()

    # Check if there are enough samples to compare
    if len(normal_expression) < 3 or len(cancer_expression) < 3:
        print('Not enough samples in one or both groups to perform statistical comparison.')
        return

    # Perform statistical test (e.g., t-test)
    #t_stat, p_value = stats.ks_2samp(normal_expression, cancer_expression)
    y_true = [0] * normal_expression.shape[0] + [1] * cancer_expression.shape[0]
    y_scores = np.concatenate([normal_expression.values, cancer_expression.values])
    auc = roc_auc_score(y_true, y_scores)
    # round to 2 decimal places
    auc = round(auc, 2)

    # Plot boxplots to compare the expression levels
    plt.figure(figsize=(8, 6))
    plt.boxplot([normal_expression, cancer_expression], labels=['Normal Uterus', 'Uterine Corpus Endometrioid Carcinoma'])
    plt.ylabel(f'{up_acc} Expression')
    plt.title(f'Comparison of {up_acc} - {gene_name} Expression\nbetween Normal Uterus and Uterine Corpus Endometrioid CarcinomaAUC: {auc:.2f}')
    
    if save_to is not None:
        plt.savefig(save_to+f'/{up_acc}_expression_comparison.png')
    
    # don't show the plot, close it
    plt.close()

    return auc, normal_expression_mean, cancer_expression_mean


def get_interactors(uniprot_string_id, up_acc, save_to=None):
    url = f"https://string-db.org/api/tsv/interaction_partners?identifiers={uniprot_string_id}&species=9606&limit=50"
    response = requests.get(url)
    response.raise_for_status()


    data = io.StringIO(response.text)
    df = pd.read_csv(data, sep='\t')
    #filter "score" > 0.9
    df = df[df['score'] > 0.9]
    df = df[['preferredName_A', 'preferredName_B', 'score']]
    # save to file
    if save_to is not None:
        df.to_csv(save_to+f'{up_acc}_interactors.tsv', sep='\t', index=False)
    
    return df

def decode_ensembl_id(ensembl_id):
    server = "https://rest.ensembl.org"
    ext = f"/xrefs/id/{ensembl_id}?"
    
    r = requests.get(server+ext, headers={ "Content-Type" : "application/json"})
    
    if not r.ok:
        r.raise_for_status()
        sys.exit()
    
    decoded = r.json()

    for r in decoded:
        if r['dbname'] == "Uniprot_gn":
            return (r['primary_id'], r['display_id'])
    return None

def get_homologs(gene_name, up_acc, save_to=None):
    server = "https://rest.ensembl.org"
    ext = f"/homology/symbol/human/{gene_name}?format=condensed;type=all;target_taxon=9606"
    
    r = requests.get(server+ext, headers={ "Content-Type" : "application/json"})
    
    if not r.ok:
        r.raise_for_status()
        sys.exit()
    
    decoded = r.json()

    homologies = []
    for d in decoded['data']:
        for h in d['homologies']:
            homologies.append(decode_ensembl_id(h['id']))
    
    df = pd.DataFrame(homologies, columns=['uniprot_id', 'gene_id'])
    # save to file
    if save_to is not None:
        df.to_csv(save_to+f'{up_acc}_homologs.tsv', sep='\t', index=False)

    return df

###################################################################
###################################################################
###################################################################
# Function to retrieve expression metrics
def get_expression_metrics(exp_results):
    if exp_results is not None and 'exp_normal' in exp_results.columns and 'exp_cancer' in exp_results.columns:
        exp_normal = exp_results['exp_normal'][0]
        exp_cancer = exp_results['exp_cancer'][0]
        fold_change = max(exp_normal, exp_cancer) / min(exp_normal, exp_cancer) if min(exp_normal, exp_cancer) != 0 else 'N/A'
        fold_change = f"{fold_change:.2f}" if isinstance(fold_change, float) else 'N/A'  # Format to two decimal places
        exp_auc = exp_results['exp_auc'][0] if 'exp_auc' in exp_results.columns else 'N/A'
        up_down_regulated = 'Upregulated' if exp_normal < exp_cancer else 'Downregulated'
    else:
        fold_change = 'N/A'
        exp_auc = 'N/A'
        up_down_regulated = 'N/A'
    return exp_auc, fold_change, up_down_regulated

# Function to count epitopes in discotope data
def count_discotope_epitopes(discotope_results):
    if discotope_results is not None and 'epitope' in discotope_results.columns:
        return discotope_results['epitope'].sum()  # Count where epitope is True
    return 'N/A'

# Function to count critical residues in aggregation data
def count_critical_aggregation_sites(agg_data):
    return len(agg_data[agg_data['Aggregation'] > 50]) if agg_data is not None else 'N/A'

# Function to get bioassemblies metrics
def get_bioassemblies_metrics(bioassemblies):
    if bioassemblies is not None and 'n_uniprots' in bioassemblies.columns and 'composition' in bioassemblies.columns:
        homo_max_n_uniprots = bioassemblies[bioassemblies['composition'] == 'Homo']['n_uniprots'].max() if 'Homo' in bioassemblies['composition'].values else 'N/A'
        hetero_max_n_uniprots = bioassemblies[bioassemblies['composition'] == 'Hetero']['n_uniprots'].max() if 'Hetero' in bioassemblies['composition'].values else 'N/A'
    else:
        homo_max_n_uniprots, hetero_max_n_uniprots = 'N/A', 'N/A'
    return homo_max_n_uniprots, hetero_max_n_uniprots

# Function to create the unified residue DataFrame
def create_unified_residue_df(discotope_results, agg_data, glycosylation_sites, modified_residues):
    # Initialize the main DataFrame with residue information from discotope
    residues_df = pd.DataFrame()

    if discotope_results is not None:
        residues_df['res'] = discotope_results['res_id'].apply(convert_to_int)  # Ensure 'res' is an integer
        residues_df['aa'] = discotope_results['residue']
        residues_df['epitope_score'] = discotope_results['DiscoTope-3.0_score']
        residues_df['epitope'] = discotope_results['epitope']
        residues_df['relative_surface_accessibility'] = discotope_results['rsa']
        residues_df['modeling_confidence'] = discotope_results['pLDDTs']
    
    # Integrate Aggregation Propensity
    if agg_data is not None:
        agg_data['res'] = agg_data['res'].apply(convert_to_int)  # Ensure 'res' is an integer
        try:
            residues_df = pd.merge(residues_df, agg_data[['res', 'Aggregation']], on='res', how='left')
        except:
            residues_df = agg_data

    # Add columns for modifications, defaulting to None
    residues_df['modification'] = None  # Start with a single 'modification' column

    # Integrate Glycosylation Sites
    if glycosylation_sites:
        glycosylation_df = pd.DataFrame(glycosylation_sites, columns=['res', 'glycosylation'])
        glycosylation_df['res'] = glycosylation_df['res'].apply(convert_to_int)  # Ensure 'res' is an integer
        try:
            residues_df = pd.merge(residues_df, glycosylation_df, on='res', how='left')
        except:
            residues_df = glycosylation_df

    # Integrate Modified Residues
    if modified_residues:
        modified_df = pd.DataFrame(modified_residues, columns=['res', 'modification'])
        modified_df['res'] = modified_df['res'].apply(convert_to_int)  # Ensure 'res' is an integer
        try:
            residues_df = pd.merge(residues_df, modified_df, on='res', how='left', suffixes=('', '_modified'))
        except:
            residues_df = modified_df

    # Resolve potential conflicts between modification columns
    if 'modification_modified' in residues_df.columns:
        # Combine 'modification' and 'modification_modified' into a single column
        residues_df['modification'] = residues_df['modification'].combine_first(residues_df['modification_modified'])
        residues_df.drop(columns=['modification_modified'], inplace=True)  # Remove the extra column

    # Fill any missing data with 'N/A'
    residues_df.fillna('N/A', inplace=True)
    
    # Ensure 'res' is sorted and handle potential None values
    residues_df = residues_df.dropna(subset=['res'])  # Remove rows with None in 'res'
    residues_df = residues_df.sort_values(by='res')

    return residues_df


# Function to format interactors and homologs
def format_interactors_homologs(data, column_name):
    if data is None or data.empty:
        return 0, 'N/A'
    
    print ()
    items = data[column_name].tolist()
    # Convert each item to a string and escape any pipe characters
    items_str = [str(item) for item in items]
    formatted_list = " \\| ".join(items_str)
    return len(items), formatted_list

def convert_html_to_markdown(html_path):
    # Read the HTML file
    with open(html_path, 'r', encoding='utf-8') as file:
        html_content = file.read()

    # Initialize the html2text converter
    converter = html2text.HTML2Text()
    converter.ignore_links = False  # Set to True if you want to ignore hyperlinks
    converter.ignore_images = True  # Set to False if you want to include image links

    # Convert HTML to Markdown
    markdown_content = converter.handle(html_content)
    return markdown_content

# Function to save the detailed markdown file
def save_detailed_markdown(up_acc, results_dir, residues_df, metrics, exp_results, glycosylation_sites, modified_residues, interactors, homologs, bioassemblies, original_data, number_of_isoforms):
    detailed_md_file = os.path.join(results_dir, f'{up_acc}_details.md')
    expression_png_path = os.path.join(results_dir, f'{up_acc}_expression_comparison.png')
    isoform_alignment_html = os.path.join(results_dir, f'{up_acc}_isoforms_alignment.html')

    with open(detailed_md_file, 'w') as detailed_file:
        detailed_file.write(f"# Detailed Data for {up_acc}\n\n")

        detailed_file.write(f"""
## Introduction to the Detailed Summary

### How to Interpret the Results

- **Summary & Metrics**: This section provides a quick reference to essential protein attributes, including expression changes, family classification, and biomarker applications. Regulation status (upregulated/downregulated) indicates the protein's behavior in a disease context. Some information comes from the original excel file with the proteins selected from literature, while others are derived from the analyses.
- **Expression Comparison**: A visual representation comparing protein expression between normal and disease states. It highlights significant changes in expression levels that might indicate diagnostic or therapeutic relevance. This is data coming from transcriptomics experiments and could not translate similarly to protein levels.
- **Isoform Alignment**: An interactive view of isoform alignments, revealing structural and functional differences between variants of the protein.
- **Interactors & Homologs**: Tables listing known interaction partners and homologous proteins, the more interactors and homologs, the more complex the protein is to design an antibody for.
- **Biological Assemblies**: Information about the structural arrangement of the protein in different assemblies, providing insights into its functional state but also the complexity of the protein to develop antibodies.
- **Combined Per-Residue Information**: A detailed table summarizing residue-level data. This includes predictions for epitope regions, aggregation tendencies, and modifications that might impact the protein's function. Each row corresponds to a residue in the protein, providing insights into specific sites that may be important for research or drug development.
""")

        # Summary & Metrics
        detailed_file.write(f"## Summary & Metrics\n\n")
        detailed_file.write(f"- **UniProt Accession**: {up_acc}\n")
        detailed_file.write(f"- **Gene Name**: {original_data['gene_name']}\n")
        detailed_file.write(f"- **Protein Name**: {original_data['protein_name']}\n")
        detailed_file.write(f"- **Swiss Prot**: {original_data['swiss_prot']}\n")
        detailed_file.write(f"- **Family**: {original_data['family']}\n")
        detailed_file.write(f"- **Biomarker Application**: {original_data['biomarker_application']}\n")
        detailed_file.write(f"- **Number of Isoforms**: {number_of_isoforms}\n")
        detailed_file.write(f"- **Regulation**: {original_data['up_down_regulated']}\n")
        detailed_file.write(f"- **(transcriptomics) AUC**: {metrics['AUC']}\n")
        detailed_file.write(f"- **(transcriptomics) Fold Change**: {metrics['Fold Change']}\n")
        detailed_file.write(f"- **(transcriptomics) Regulation**: {metrics['Up/Down Regulated']}\n")
        detailed_file.write(f"- **Discotope Epitope Count**: {metrics['Discotope Epitope Count']}\n")
        detailed_file.write(f"- **Max n_uniprots (Homo)**: {metrics['Max n_uniprots Homo']}\n")
        detailed_file.write(f"- **Max n_uniprots (Hetero)**: {metrics['Max n_uniprots Hetero']}\n")
        detailed_file.write("\n\n")
        
        # Expression Comparison Image
        if os.path.exists(expression_png_path):
            detailed_file.write(f"## Expression Comparison\n\n")
            detailed_file.write(f"![Expression Comparison]({f'./{up_acc}_expression_comparison.png'})\n\n")
        
        # Isoform Alignment Iframe
        if os.path.exists(isoform_alignment_html):
            with open(isoform_alignment_html, 'r', encoding='utf-8') as file:
                    html_content = file.read()
            detailed_file.write(f"## Isoform Alignment\n\n")
            detailed_file.write(f"<div>\n{html_content}\n</div>\n\n")

        # Interactors
        if interactors is not None:
            detailed_file.write(f"## Interactors\n\n")
            detailed_file.write(interactors.to_markdown(index=False))
            detailed_file.write("\n\n")
            
        # Homologs
        if homologs is not None:
            detailed_file.write(f"## Homologs\n\n")
            detailed_file.write(homologs.to_markdown(index=False))
            detailed_file.write("\n\n")
        
        # Biological Assemblies
        if bioassemblies is not None:
            detailed_file.write(f"## Biological Assemblies\n\n")
            detailed_file.write(bioassemblies.to_markdown(index=False))
            detailed_file.write("\n\n")

        # Combined Per-Residue Information
        detailed_file.write(f"## Combined Per-Residue Information\n\n")
        detailed_file.write(residues_df.to_markdown(index=False))
        detailed_file.write("\n\n")



def convert_to_int(value):
    try:
        return int(value)
    except ValueError:
        print(f"Warning: Unable to convert {value} to integer.")
        return None  # or an appropriate default

# Function to save the general markdown file
def save_general_markdown(summary_df, base_dir):
    general_md_file = os.path.join(base_dir, "general_summary.md")
    
    # Modify the Uniprot ID column to include Markdown links directly
    summary_df['Uniprot ID'] = summary_df['Uniprot ID'].apply(
        lambda x: f"[{x}](./{x[0:2]}/{x}/{x}_details.md)"
    )

    with open(general_md_file, 'w') as general_file:
        general_file.write("# General Summary of Protein Data\n\n")

        general_file.write("""
## Introduction to the General Summary

This summary provides an overview of the protein analyses results obtained through the use of various bioinformatics tools. 
The proteins where selected from the set of 506 proteins obtained from literature review as potential antigens for uterine carcinosarcoma.
Each protein analyzed is represented in the table below, with detailed information provided for each entry (a few entries have failed
when computing the pipeline and they will be manually reviewed, but is a very small minority). 


This document aims to provide a quick and comprehensive summary of the key metrics and findings for each protein, serving as an entry point
to more in-depth analyses.

### Tools Utilized
- **UniProt XML file**: Used to gather protein-specific information, including isoforms, biological attributes and identifiers in other databases.
- **Discotope 3.0**: Utilized for predicting potential epitope regions based on structural data.
- **Tango**: Conducted to assess the likelihood of residue-level aggregation.
- **Expression Data**: A comparison of protein expression levels across normal and disease states whas obtained from GTEX and TCGA using biomart API.
- **Isoform Analysis**: Alignment of protein isoforms to identify structural and functional differences was performed with BioPython.
- **STRING-DB API**: Used to retrieve interactors and homologous proteins for each target.
- **Ensembl REST API**: Employed to decode Ensembl IDs and retrieve homologous human proteins.
- **AlphaFold**: Used to obtain full structural data for the proteins (modelled).
- **PDB**: Used to obtain structural data for the proteins, particularly biological assemblies.

### How to Interpret the Results
- **Uniprot ID**: A clickable link to access detailed information for each protein.
- **AUC**: Indicates the accuracy of distinguishing normal from disease states based on expression data. A higher value suggests better discriminatory power. *This information is based on transcriptomics data from GTEX and TCGA and could not behave in the same way for proteins.*
- **Fold Change**: A measure of the difference in expression levels between conditions. Values greater than 1.0 indicate upregulation. High AUCs with small fold changes may indicate consistent differences but subtle ones and could be hard to see differences at protein level.
- **Up/Down regulation**: -1 for downregulated, 1 for upregulated, 2 for both, in the first column expressing this, coming from the literature. On the transcriptomics column: values, if available, from GTEX and TCGA, that could or could not could not behave in the same way for proteins.
- **Glycosylation Sites & Modified Residues**: Numbers of residues that could undergo to specific modifications that block their access by the antibodies when developing the assays.
- **Discotope Epitope Count**: The number of residues predicted to be part of epitopes, important for immunogenicity studies, but what is important is to observe them in the structure.
- **Interactor Count & Homolog Count**: Quantitative data on interactors and homologous proteins. Homologs are just computed from human proteins, this analysis could be extended to other organsims if necessary. High number of interactors and homologs are not preffered.
- **Isoforms**: The total number of protein isoforms analyzed, which may indicate structural or functional diversity.
- **Aggregation Sites**: Number of residues with high aggregation propensity, which could affect protein stability and function.
- **Biological Assemblies**: The maximum number of UniProt IDs in a biological assembly (heterodimers) and count of the same Uniprot ID in a biological assembly (homodimers). This provide insights into protein complexes beyond binary interactions marked in STRING database. The higher the number of uniprot IDs in a biological assembly or the homodimer count, the more complex the protein to design an antibody for.

Please refer to the individual detailed summaries for each protein for a deeper examination of residue-level information and specific analyses.
""")

        # Create a markdown table from the modified summary DataFrame
        general_file.write(summary_df.to_markdown(index=False))
        general_file.write("\n\n")
