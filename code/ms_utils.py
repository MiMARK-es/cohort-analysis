import pandas as pd
import numpy as np
from sklearn.metrics import roc_auc_score, roc_curve
from scipy.stats import mannwhitneyu
from statsmodels.stats.multitest import multipletests

def load_data_with_metadata(data_path, metadata_path, key_column):
    df_metadata = pd.read_csv(metadata_path, sep='\t', index_col=key_column, header=0)
    # The data has a multi-index with the protein and the peptide
    df_data = pd.read_csv(data_path, sep='\t', index_col=[0,1], header=0)
    # We will keep only the proteins and rename the columns to indicate the peptide number
    df_data.index = df_data.index.droplevel(1)
    # Join the dataframes
    df_ret = df_metadata.join(df_data.T, how='inner')
    # remove rows with not_use != NaN
    df_ret = df_ret[df_ret['not_use'].isna()]
    return df_ret

# Function to rename duplicated columns
def rename_duplicated_columns(df):
    cols = pd.Series(df.columns)
    for dup in cols[cols.duplicated()].unique():
        cols[cols[cols == dup].index.values.tolist()] = [dup + '_' + str(i) for i in range(sum(cols == dup))]
    df.columns = cols
    return df


################# COHORT 7.3 UTILS #################

def load_7_3_pg_matrix(
    pg_matrix_path,
    metadata_path,
    nan_thresh=None,
    log2_transform=True,
    median_normalize=False
):
    """
    Load and preprocess the PG matrix and metadata.

    Args:
        pg_matrix_path (str): Path to the PG matrix CSV file.
        metadata_path (str): Path to the metadata CSV file.
        nan_thresh (int): Minimum number of non-NaN values required to keep a sample.
        log2_transform (bool): Whether to apply log2 transformation.
        median_normalize (bool): Whether to median-normalize each sample.

    Returns:
        df (pd.DataFrame): Preprocessed PG matrix with metadata columns.
    """
    # Load PG matrix
    df = pd.read_csv(pg_matrix_path, index_col='Protein.Names', header=0, sep='\t')

    # Harmonize sample names
    df.columns = list(df.columns[0:3]) + [
        c.replace('/users/pr/rawstream/2025NK011/mzml/', '')[0:len("2025NK011_EVCO_001")]
        for c in df.columns[3:]
    ]

    # Convert to numeric and replace zeros with NaN
    df.iloc[:, 3:] = df.iloc[:, 3:].replace(0, np.nan)
    df.iloc[:, 3:] = df.iloc[:, 3:].apply(pd.to_numeric, errors='coerce')

    # Remove first 3 columns, keep only protein data
    df = df.iloc[:, 3:]

    # Log2 transform
    if log2_transform:
        df = np.log2(df)

    # Transpose: rows=samples, columns=proteins
    df = df.T

    # Discard samples with too many NaNs
    if nan_thresh is not None:
        df = df.dropna(thresh=nan_thresh)

    # Median normalization
    if median_normalize:
        #df = df.subtract(df.median(axis=1), axis=0)
        global_median = df.stack().median()        # median of all log2 values (across all samples/proteins)
        sample_medians = df.median(axis=1)        # median per sample (row)
        correction = sample_medians - global_median  # how much each sample deviates
        df = df.subtract(correction, axis=0)       # subtract correction per row

    # Load metadata and merge
    df_metadata = pd.read_csv(metadata_path, index_col='id_ms', header=0, sep='\t')
    df['Pathology'] = df_metadata['Pathology']
    df['Endometrial_thickness'] = df_metadata['Endometrial_thickness']
    df['sample'] = df_metadata['sample']
    df['Grade'] = df_metadata['Grade']
    df['Type'] = df_metadata['Type']
    df['Stage'] = df_metadata['Stage']

    # Drop samples without pathology
    df = df.dropna(subset=['Pathology'])

    # Make sample column from metadata the index of df
    df = df.set_index('sample')

    df.Pathology = df.Pathology.map({'Benign': 0, 'EC': 1})

    return df

def compute_ms_biomarker_metrics(df):
    """
    Compute AUC, sensitivity, specificity, log2FC, sample counts, and adjusted p-values for each biomarker.
    """
    from sklearn.metrics import roc_auc_score, roc_curve

    df = df.copy()

    auc_scores = {}
    sensitivity_max_sum = {}
    specificity_max_sum = {}
    sensitivity_high = {}
    specificity_for_high_sens = {}
    log2FC = {}
    n_pos = {}
    n_neg = {}
    pvalues = {}

    biomarkers = [col for col in df.columns if col not in ['Pathology', 'Endometrial_thickness', 'Grade', 'Type', 'Stage']]

    for biomarker in biomarkers:
        if df[biomarker].isnull().all():
            continue

        y_true = df.Pathology[df[biomarker].notnull()]
        y_score = df[biomarker][df[biomarker].notnull()]

        if len(y_true) == 0 or len(y_score) == 0:
            continue

        auc = roc_auc_score(y_true, y_score)

        # Invert if needed
        if auc < 0.5:
            auc = 1 - auc
            y_score = -y_score

        fpr, tpr, thresholds = roc_curve(y_true, y_score)
        specificity = 1 - fpr

        # Max sum criterion
        sum_sens_spec = tpr + specificity
        optimal_idx = np.argmax(sum_sens_spec)

        # High sensitivity criterion
        high_sens_indices = np.where(tpr >= 0.95)[0]
        if len(high_sens_indices) > 0:
            high_sens_optimal_idx = high_sens_indices[np.argmax(specificity[high_sens_indices])]
            sens_high = tpr[high_sens_optimal_idx]
            spec_high = specificity[high_sens_optimal_idx]
        else:
            sens_high = np.nan
            spec_high = np.nan

        # Log2FC
        means = df[biomarker].groupby(df['Pathology']).mean()
        if 0 in means and 1 in means:
            log2fc = means[1] - means[0]
        else:
            log2fc = np.nan

        # Mann-Whitney U test for p-value
        group0 = df[df.Pathology == 0][biomarker].dropna()
        group1 = df[df.Pathology == 1][biomarker].dropna()
        if len(group0) > 0 and len(group1) > 0:
            try:
                stat, pval = mannwhitneyu(group0, group1, alternative='two-sided')
            except Exception:
                pval = np.nan
        else:
            pval = np.nan

        auc_scores[biomarker] = round(float(auc), 3)
        sensitivity_max_sum[biomarker] = round(float(tpr[optimal_idx]), 3)
        specificity_max_sum[biomarker] = round(float(specificity[optimal_idx]), 3)
        sensitivity_high[biomarker] = round(float(sens_high), 3)
        specificity_for_high_sens[biomarker] = round(float(spec_high), 3)
        log2FC[biomarker] = round(float(log2fc), 3)
        n_pos[biomarker] = df[df.Pathology == 1][biomarker].count()
        n_neg[biomarker] = df[df.Pathology == 0][biomarker].count()
        pvalues[biomarker] = pval

    # Adjust p-values
    biomarker_list = list(auc_scores.keys())
    raw_pvals = [pvalues[b] for b in biomarker_list]

    # Replace NaN with 1.0 for adjustment, keep track of NaN positions
    raw_pvals_for_adj = [p if not np.isnan(p) else 1.0 for p in raw_pvals]
    adj_pvals = multipletests(raw_pvals_for_adj, method='fdr_bh')[1]
    # Set adj_pvals to NaN where original pvalue was NaN
    adj_pvals = [adj if not np.isnan(raw) else np.nan for adj, raw in zip(adj_pvals, raw_pvals)]

    # Assemble results
    result_df = pd.DataFrame({
        'AUC': [auc_scores[b] for b in biomarker_list],
        'Sensitivity (max sum)': [sensitivity_max_sum[b] for b in biomarker_list],
        'Specificity (max sum)': [specificity_max_sum[b] for b in biomarker_list],
        'Sensitivity (sens > 95%)': [sensitivity_high[b] for b in biomarker_list],
        'Specificity (sens > 95%)': [specificity_for_high_sens[b] for b in biomarker_list],
        'Log2FC': [log2FC[b] for b in biomarker_list],
        'n_pos': [n_pos[b] for b in biomarker_list],
        'n_neg': [n_neg[b] for b in biomarker_list],
        'pvalue': raw_pvals,
        'adj_pvalue': adj_pvals
    }, index=biomarker_list)

    # Format p-values in scientific notation with three decimals
    result_df['pvalue'] = result_df['pvalue'].apply(lambda x: f"{x:.3e}" if pd.notnull(x) else np.nan)
    result_df['adj_pvalue'] = result_df['adj_pvalue'].apply(lambda x: f"{x:.3e}" if pd.notnull(x) else np.nan)

    return result_df


################# ENDODX UTILS #################

def load_endodx_pg_matrix(
    pg_matrix_path,
    metadata_path,
    nan_thresh=None,
    log2_transform=True,
    median_normalize=False
):
    """
    Load and preprocess the endoDx PG matrix and metadata.

    Args:
        pg_matrix_path (str): Path to the PG matrix CSV file.
        metadata_path (str): Path to the metadata CSV file.
        nan_thresh (int): Minimum number of non-NaN values required to keep a sample.
        log2_transform (bool): Whether to apply log2 transformation.
        median_normalize (bool): Whether to median-normalize each sample.

    Returns:
        tuple: (df, biomarkers, metavariables)
            df (pd.DataFrame): Preprocessed PG matrix with metadata columns.
            biomarkers (list): List of biomarker column names from the PG matrix.
            metavariables (list): List of metadata column names.
    """
    # Load PG matrix
    df = pd.read_csv(pg_matrix_path, index_col='Protein.Names', header=0)

    # Harmonize sample names - extract the EVCO part from the long paths
    new_cols = list(df.columns[0:5])
    for c in df.columns[5:]:
        # Extract sample ID from the path
        if '2024MK046_EVCO_' in c:
            sample_id = c.split('2024MK046_EVCO_')[1].split('_')[0]
            new_cols.append(f"2024MK046_EVCO_{sample_id}")
        else:
            new_cols.append(str(c))
    df.columns = new_cols

    # Convert to numeric and replace zeros with NaN
    df.iloc[:, 5:] = df.iloc[:, 5:].replace(0, np.nan)
    df.iloc[:, 5:] = df.iloc[:, 5:].apply(pd.to_numeric, errors='coerce')

    # Store biomarker names (protein names from the original matrix)
    biomarkers = df.index.tolist()

    # Remove first 5 columns, keep only protein data
    df = df.iloc[:, 5:]

    # Log2 transform
    if log2_transform:
        df = np.log2(df)

    # Transpose: rows=samples, columns=proteins
    df = df.T
    
    # Discard samples with too many NaNs
    if nan_thresh is not None:
        df = df.dropna(thresh=nan_thresh)

    # Median normalization
    if median_normalize:
        global_median = df.stack().median()        # median of all log2 values (across all samples/proteins)
        sample_medians = df.median(axis=1)        # median per sample (row)
        correction = sample_medians - global_median  # how much each sample deviates
        df = df.subtract(correction, axis=0)       # subtract correction per row

    # Load metadata and merge
    df_metadata = pd.read_csv(metadata_path, index_col='Codigo_CRG', header=0, sep='\t')
    
    # Map Spanish groups to binary
    grupo_mapping = {'Control': 0, 'Endometriosis': 1}
    
    # Add metadata columns to samples that exist in both datasets
    common_samples = df.index.intersection(df_metadata.index)
    df = df.loc[common_samples]
    
    # Define metadata variables list
    metavariables = ['Codigo_VHIR', 'Codigo_CRG', 'Vol_inicial', 'Conc_Prote', 'Digestion_ug', 
                     'Vol_digestion', 'Centro', 'Lugar', 'Fecha_proce', 'Fecha_reco', 'Tiempo_proce',
                     'Edad', 'Subgrupo', 'Tipo_tto', 'Sintomatologia', 'VAS_dolor', 'Causa_infertilidad',
                     'Otras_enfermedades', 'Grupo', 'Endometriosis_subtipo', 'Previa_cito', 'Lubricante',
                     'Previa_TVUS', 'Hemolisis', 'IMC', 'Previa_cirugia']
    
    # Add all metadata columns
    df['Codigo_VHIR'] = df_metadata.loc[common_samples, 'Codigo_VHIR']
    df['Codigo_CRG'] = common_samples  # This is the index, so we add it as a column
    df['Vol_inicial'] = df_metadata.loc[common_samples, 'Vol_inicial']
    df['Conc_Prote'] = df_metadata.loc[common_samples, 'Conc_Prote']
    df['Digestion_ug'] = df_metadata.loc[common_samples, 'Digestion_ug']
    df['Vol_digestion'] = df_metadata.loc[common_samples, 'Vol_digestion']
    df['Centro'] = df_metadata.loc[common_samples, 'Centro']
    df['Lugar'] = df_metadata.loc[common_samples, 'Lugar']
    df['Fecha_proce'] = df_metadata.loc[common_samples, 'Fecha_proce']
    df['Fecha_reco'] = df_metadata.loc[common_samples, 'Fecha_reco']
    df['Tiempo_proce'] = df_metadata.loc[common_samples, 'Tiempo_proce']
    df['Edad'] = df_metadata.loc[common_samples, 'Edad']
    df['Subgrupo'] = df_metadata.loc[common_samples, 'Subgrupo']
    df['Tipo_tto'] = df_metadata.loc[common_samples, 'Tipo_tto']
    df['Sintomatologia'] = df_metadata.loc[common_samples, 'Sintomatologia']
    df['VAS_dolor'] = df_metadata.loc[common_samples, 'VAS_dolor']
    df['Causa_infertilidad'] = df_metadata.loc[common_samples, 'Causa_infertilidad']
    df['Otras_enfermedades'] = df_metadata.loc[common_samples, 'Otras_enfermedades']
    df['Grupo'] = df_metadata.loc[common_samples, 'Grupo'].map(grupo_mapping)
    df['Endometriosis_subtipo'] = df_metadata.loc[common_samples, 'Endometriosis_subtipo']
    df['Previa_cito'] = df_metadata.loc[common_samples, 'Previa_cito']
    df['Lubricante'] = df_metadata.loc[common_samples, 'Lubricante']
    df['Previa_TVUS'] = df_metadata.loc[common_samples, 'Previa_TVUS']
    df['Hemolisis'] = df_metadata.loc[common_samples, 'Hemolisis']
    df['IMC'] = df_metadata.loc[common_samples, 'IMC']
    df['Previa_cirugia'] = df_metadata.loc[common_samples, 'Previa_cirugia']

    # Filter biomarkers to only include those present in the final dataframe
    biomarkers = [b for b in biomarkers if b in df.columns]

    return df, biomarkers, metavariables

def compute_endodx_biomarker_metrics(df):
    """
    Compute AUC, sensitivity, specificity, log2FC, sample counts, and adjusted p-values for each biomarker
    in the endoDx dataset (Control vs Endometriosis).
    """
    from sklearn.metrics import roc_auc_score, roc_curve

    df = df.copy()

    auc_scores = {}
    sensitivity_max_sum = {}
    specificity_max_sum = {}
    sensitivity_high = {}
    specificity_for_high_sens = {}
    log2FC = {}
    n_control = {}
    n_endometriosis = {}
    pvalues = {}

    # Get biomarker columns (exclude metadata columns)
    metadata_cols = ['Codigo_VHIR', 'Codigo_CRG', 'Vol_inicial', 'Conc_Prote', 'Digestion_ug', 
                     'Vol_digestion', 'Centro', 'Lugar', 'Fecha_proce', 'Fecha_reco', 'Tiempo_proce',
                     'Edad', 'Subgrupo', 'Tipo_tto', 'Sintomatologia', 'VAS_dolor', 'Causa_infertilidad',
                     'Otras_enfermedades', 'Grupo', 'Endometriosis_subtipo', 'Previa_cito', 'Lubricante',
                     'Previa_TVUS', 'Hemolisis', 'IMC', 'Previa_cirugia']
    biomarkers = [col for col in df.columns if col not in metadata_cols]

    for biomarker in biomarkers:
        if df[biomarker].isnull().all():
            continue

        # Get valid data for this biomarker
        valid_data = df[df[biomarker].notnull()].copy()
        if len(valid_data) == 0:
            continue
            
        y_true = valid_data['Grupo']
        y_score = valid_data[biomarker]

        # Check if we have both classes
        unique_classes = y_true.unique()
        if len(unique_classes) < 2:
            continue

        try:
            auc = roc_auc_score(y_true, y_score)

            # Invert if needed
            if auc < 0.5:
                auc = 1 - auc
                y_score = -y_score

            fpr, tpr, thresholds = roc_curve(y_true, y_score)
            specificity = 1 - fpr

            # Max sum criterion
            sum_sens_spec = tpr + specificity
            optimal_idx = np.argmax(sum_sens_spec)

            # High sensitivity criterion
            high_sens_indices = np.where(tpr >= 0.95)[0]
            if len(high_sens_indices) > 0:
                high_sens_optimal_idx = high_sens_indices[np.argmax(specificity[high_sens_indices])]
                sens_high = tpr[high_sens_optimal_idx]
                spec_high = specificity[high_sens_optimal_idx]
            else:
                sens_high = np.nan
                spec_high = np.nan

            # Log2FC
            means = valid_data[biomarker].groupby(valid_data['Grupo']).mean()
            if 0 in means and 1 in means:
                log2fc = means[1] - means[0]
            else:
                log2fc = np.nan

            # Mann-Whitney U test for p-value
            group0 = valid_data[valid_data['Grupo'] == 0][biomarker].dropna()  # Control
            group1 = valid_data[valid_data['Grupo'] == 1][biomarker].dropna()  # Endometriosis
            if len(group0) > 0 and len(group1) > 0:
                try:
                    stat, pval = mannwhitneyu(group0, group1, alternative='two-sided')
                except Exception:
                    pval = np.nan
            else:
                pval = np.nan

            auc_scores[biomarker] = round(float(auc), 3)
            sensitivity_max_sum[biomarker] = round(float(tpr[optimal_idx]), 3)
            specificity_max_sum[biomarker] = round(float(specificity[optimal_idx]), 3)
            sensitivity_high[biomarker] = round(float(sens_high), 3)
            specificity_for_high_sens[biomarker] = round(float(spec_high), 3)
            log2FC[biomarker] = round(float(log2fc), 3)
            n_control[biomarker] = len(group0)
            n_endometriosis[biomarker] = len(group1)
            pvalues[biomarker] = pval
            
        except Exception as e:
            # Skip biomarkers that cause errors
            continue

    # Adjust p-values
    biomarker_list = list(auc_scores.keys())
    raw_pvals = [pvalues[b] for b in biomarker_list]

    # Replace NaN with 1.0 for adjustment, keep track of NaN positions
    raw_pvals_for_adj = [p if not np.isnan(p) else 1.0 for p in raw_pvals]
    if len(raw_pvals_for_adj) > 0:
        adj_pvals = multipletests(raw_pvals_for_adj, method='fdr_bh')[1]
        # Set adj_pvals to NaN where original pvalue was NaN
        adj_pvals = [adj if not np.isnan(raw) else np.nan for adj, raw in zip(adj_pvals, raw_pvals)]
    else:
        adj_pvals = []

    # Assemble results
    result_df = pd.DataFrame({
        'AUC': [auc_scores[b] for b in biomarker_list],
        'Sensitivity (max sum)': [sensitivity_max_sum[b] for b in biomarker_list],
        'Specificity (max sum)': [specificity_max_sum[b] for b in biomarker_list],
        'Sensitivity (sens > 95%)': [sensitivity_high[b] for b in biomarker_list],
        'Specificity (sens > 95%)': [specificity_for_high_sens[b] for b in biomarker_list],
        'Log2FC': [log2FC[b] for b in biomarker_list],
        'n_control': [n_control[b] for b in biomarker_list],
        'n_endometriosis': [n_endometriosis[b] for b in biomarker_list],
        'pvalue': raw_pvals,
        'adj_pvalue': adj_pvals
    }, index=biomarker_list)

    # Format p-values in scientific notation with three decimals
    result_df['pvalue'] = result_df['pvalue'].apply(lambda x: f"{x:.3e}" if pd.notnull(x) else np.nan)
    result_df['adj_pvalue'] = result_df['adj_pvalue'].apply(lambda x: f"{x:.3e}" if pd.notnull(x) else np.nan)

    return result_df