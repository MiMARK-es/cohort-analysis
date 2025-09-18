"""
EndoDx-specific utilities for mass spectrometry data analysis.

This module contains functions specifically designed for the EndoDx study,
including data loading, normalization, and analysis functions.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import roc_auc_score, roc_curve, silhouette_score
from scipy.stats import ttest_ind, f_oneway
from statsmodels.stats.multitest import multipletests
from statsmodels.nonparametric.smoothers_lowess import lowess


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
    
    # Set the index name to 'sample' after transposing
    df.index.name = 'sample'

    # Discard samples with too many NaNs
    if nan_thresh is not None:
        df = df.dropna(thresh=nan_thresh)

    # Median normalization
    if median_normalize:
        global_median = df.stack().median()
        sample_medians = df.median(axis=1)
        correction = sample_medians - global_median
        df = df.subtract(correction, axis=0)

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
    for var in metavariables:
        if var == 'Codigo_CRG':
            df[var] = common_samples
        elif var in df_metadata.columns:
            if var == 'Grupo':
                df[var] = df_metadata.loc[common_samples, var].map(grupo_mapping)
            else:
                df[var] = df_metadata.loc[common_samples, var]

    # Drop samples without pathology group
    df = df.dropna(subset=['Grupo'])

    # Filter biomarkers to only include those present in the final dataframe
    biomarkers = [b for b in biomarkers if b in df.columns]

    return df, biomarkers, metavariables


def filter_biomarkers_by_detection(data, biomarkers, detection_threshold=0.75, silent=False):
    """
    Filter biomarkers based on detection percentage across samples.
    
    Args:
        data (pd.DataFrame): DataFrame with samples and biomarker intensities
        biomarkers (list): List of biomarker column names
        detection_threshold (float): Minimum percentage of samples where biomarker must be detected (not NaN)
    
    Returns:
        tuple: (filtered_biomarkers, detection_stats)
            filtered_biomarkers (list): List of biomarkers that meet the detection threshold
            detection_stats (pd.DataFrame): DataFrame with detection statistics for all biomarkers
    """
    if not silent:
        print(f"Filtering biomarkers with detection threshold: {detection_threshold*100}%")
    
    # Calculate detection percentage for each biomarker
    detection_stats = []
    n_samples = len(data)
    
    for biomarker in biomarkers:
        if biomarker in data.columns:
            # Count non-NaN values
            detected_count = data[biomarker].notna().sum()
            detection_percentage = detected_count / n_samples
            
            detection_stats.append({
                'biomarker': biomarker,
                'detected_samples': detected_count,
                'total_samples': n_samples,
                'detection_percentage': detection_percentage,
                'passes_threshold': detection_percentage >= detection_threshold
            })
    
    detection_df = pd.DataFrame(detection_stats)
    
    # Filter biomarkers that meet the threshold
    filtered_biomarkers = detection_df[detection_df['passes_threshold']]['biomarker'].tolist()

    if not silent:
        print(f"Original biomarkers: {len(biomarkers)}")
        print(f"Filtered biomarkers (≥{detection_threshold*100}% detection): {len(filtered_biomarkers)}")
        print(f"Removed biomarkers: {len(biomarkers) - len(filtered_biomarkers)}")

        # Show detection statistics summary
        print(f"\nDetection percentage distribution:")
        print(f"  Mean: {detection_df['detection_percentage'].mean():.3f}")
        print(f"  Median: {detection_df['detection_percentage'].median():.3f}")
        print(f"  Min: {detection_df['detection_percentage'].min():.3f}")
        print(f"  Max: {detection_df['detection_percentage'].max():.3f}")
    
    return filtered_biomarkers, detection_df


def plot_detection_analysis(detection_stats, detection_threshold, figsize=(15, 5)):
    """
    Create visualization of biomarker detection statistics.
    
    Args:
        detection_stats (pd.DataFrame): Detection statistics DataFrame from filter_biomarkers_by_detection
        detection_threshold (float): Detection threshold used for filtering
        figsize (tuple): Figure size
        
    Returns:
        matplotlib.figure.Figure: The detection analysis figure
    """
    fig, axes = plt.subplots(1, 2, figsize=figsize)

    # Histogram of detection percentages
    axes[0].hist(detection_stats['detection_percentage'], bins=50, alpha=0.7, color='skyblue', edgecolor='black')
    axes[0].axvline(detection_threshold, color='red', linestyle='--', linewidth=2, 
                    label=f'Threshold ({detection_threshold*100}%)')
    axes[0].set_xlabel('Detection Percentage')
    axes[0].set_ylabel('Number of Biomarkers')
    axes[0].set_title('Distribution of Biomarker Detection Percentages')
    axes[0].legend()
    axes[0].grid(True, alpha=0.3)

    # Bar plot comparing before/after filtering
    n_original = len(detection_stats)
    n_filtered = detection_stats['passes_threshold'].sum()
    n_removed = n_original - n_filtered
    
    categories = ['Original\nBiomarkers', 'Filtered\nBiomarkers', 'Removed\nBiomarkers']
    counts = [n_original, n_filtered, n_removed]
    colors = ['lightblue', 'lightgreen', 'lightcoral']

    bars = axes[1].bar(categories, counts, color=colors, alpha=0.7, edgecolor='black')
    axes[1].set_ylabel('Number of Biomarkers')
    axes[1].set_title(f'Biomarker Filtering Results (≥{detection_threshold*100}% threshold)')

    # Add value labels on bars
    for bar, count in zip(bars, counts):
        height = bar.get_height()
        axes[1].text(bar.get_x() + bar.get_width()/2., height + max(counts)*0.01,
                    f'{count}', ha='center', va='bottom', fontweight='bold')

    plt.tight_layout()
    return fig


def apply_mean_normalization(data, biomarkers):
    """
    Apply mean-centered normalization to biomarker data.
    
    Args:
        data (pd.DataFrame): Input dataframe with biomarker columns
        biomarkers (list): List of biomarker column names
        
    Returns:
        pd.DataFrame: Data with mean-normalized biomarkers
    """
    data_norm = data.copy()
    biomarker_data = data_norm[biomarkers]
    global_mean = biomarker_data.stack().mean()
    sample_means = biomarker_data.mean(axis=1)
    correction = sample_means - global_mean
    data_norm.loc[:, biomarkers] = biomarker_data.subtract(correction, axis=0)
    return data_norm

def apply_lowess_normalization(data, biomarkers, frac=0.6):
    """
    Apply LOWESS normalization based on M-A plots, a standard method for
    correcting intensity-dependent bias in proteomics/genomics data.

    Args:
        data (pd.DataFrame): Input dataframe with log2-transformed intensities.
        biomarkers (list): List of biomarker column names.
        frac (float): Fraction of data to use in LOWESS smoothing.

    Returns:
        pd.DataFrame: Data with LOWESS-normalized biomarkers.
    """
    data_norm = data.copy()
    biomarker_data = data_norm[biomarkers]

    # Important: This method assumes data is on a log2 scale.
    # If not, you must transform it first: biomarker_data = np.log2(biomarker_data)

    # 1. Create a reference sample (pseudo-median sample)
    reference_sample = biomarker_data.median(axis=0).values
    
    normalized_matrix = np.zeros_like(biomarker_data.values)

    # 2. Iterate through each sample and normalize it against the reference
    for i, (sample_idx, sample_series) in enumerate(biomarker_data.iterrows()):
        sample_values = sample_series.values
        
        # Keep track of non-missing values
        valid_mask = np.isfinite(sample_values) & np.isfinite(reference_sample)
        
        # 3. Calculate M and A values
        M = sample_values[valid_mask] - reference_sample[valid_mask]
        A = 0.5 * (sample_values[valid_mask] + reference_sample[valid_mask])
        
        # 4. Fit LOWESS curve to the M-A plot
        # The x-values for lowess are the average intensities (A)
        # The y-values are the log-ratios (M)
        # We sort by A to ensure the smoother works correctly
        sort_order = np.argsort(A)
        lowess_fit = lowess(M[sort_order], A[sort_order], frac=frac, return_sorted=False)
        
        # Unsort the correction factor to match original protein order
        correction = np.zeros_like(M)
        correction[sort_order] = lowess_fit
        
        # 5. Apply the correction
        corrected_values = sample_values.copy()
        corrected_values[valid_mask] -= correction
        
        normalized_matrix[i, :] = corrected_values
        
    # Put the normalized data back into the DataFrame
    data_norm[biomarkers] = pd.DataFrame(normalized_matrix, 
                                         index=biomarker_data.index, 
                                         columns=biomarker_data.columns)

    return data_norm

def perform_pca_analysis(data, biomarkers, metavariables, title="PCA Analysis", ax=None):
    """
    Perform PCA analysis and create visualization.
    
    Args:
        data (pd.DataFrame): Input data
        biomarkers (list): List of biomarker columns
        metavariables (list): List of metadata columns
        title (str): Title for the plot
        ax: Matplotlib axis object (optional)
        
    Returns:
        tuple: (pca_result_df, pca_object, explained_variance_ratio)
    """
    # Standardize and perform PCA
    scaler = StandardScaler()
    data_scaled = scaler.fit_transform(data[biomarkers].fillna(0))
    pca = PCA(n_components=2)
    pca_result = pca.fit_transform(data_scaled)
    
    # Create PCA dataframe
    df_pca = pd.DataFrame(data=pca_result, columns=['PC1', 'PC2'], index=data.index)
    df_pca = df_pca.join(data[metavariables])
    
    # Plot PCA if axis provided
    if ax is not None:
        sns.scatterplot(data=df_pca, x='PC1', y='PC2', hue='Grupo', ax=ax)
        ax.set_title(title)
        ax.set_xlabel(f'PC1 ({pca.explained_variance_ratio_[0]*100:.1f}% Variance)')
        ax.set_ylabel(f'PC2 ({pca.explained_variance_ratio_[1]*100:.1f}% Variance)')
        
        # Update legend
        handles, labels = ax.get_legend_handles_labels()
        ax.legend(handles, ['Control', 'Endometriosis'])
    
    return df_pca, pca, pca.explained_variance_ratio_


def calculate_normalization_metrics(data, biomarkers):
    """
    Calculate comprehensive normalization effectiveness metrics.
    
    Args:
        data (pd.DataFrame): Input data
        biomarkers (list): List of biomarker columns
        
    Returns:
        dict: Dictionary containing various normalization metrics
    """
    # Calculate various metrics
    sample_means = data[biomarkers].mean(axis=1).dropna()
    sample_medians = data[biomarkers].median(axis=1).dropna()
    sample_stds = data[biomarkers].std(axis=1).dropna()
    sample_mads = data[biomarkers].apply(lambda x: np.median(np.abs(x - x.median())), axis=1).dropna()
    
    # Intensity-dependent variance
    protein_means = data[biomarkers].mean(axis=0).dropna()
    protein_vars = data[biomarkers].var(axis=0).dropna()
    
    # Only use proteins that have valid means and variances
    common_proteins = protein_means.index.intersection(protein_vars.index)
    protein_means_clean = protein_means[common_proteins]
    protein_vars_clean = protein_vars[common_proteins]
    
    # Remove any remaining NaN or infinite values
    finite_mask = np.isfinite(protein_means_clean) & np.isfinite(protein_vars_clean)
    protein_means_final = protein_means_clean[finite_mask]
    protein_vars_final = protein_vars_clean[finite_mask]
    
    if len(protein_means_final) > 1:
        mean_var_corr = np.corrcoef(protein_means_final, protein_vars_final)[0, 1]
    else:
        mean_var_corr = 0.0
    
    # Pooled CV (within-group variability)
    try:
        control_data = data[data['Grupo'] == 0][biomarkers]
        endo_data = data[data['Grupo'] == 1][biomarkers]
        
        # Calculate CV for each group, handling division by zero
        control_means = control_data.mean(axis=0)
        control_stds = control_data.std(axis=0)
        endo_means = endo_data.mean(axis=0)
        endo_stds = endo_data.std(axis=0)
        
        # Only calculate CV where mean is not zero or very small
        valid_control = (np.abs(control_means) > 1e-10) & np.isfinite(control_means) & np.isfinite(control_stds)
        valid_endo = (np.abs(endo_means) > 1e-10) & np.isfinite(endo_means) & np.isfinite(endo_stds)
        
        if np.sum(valid_control) > 0:
            control_cv = (control_stds[valid_control] / control_means[valid_control]).median()
        else:
            control_cv = 0.0
            
        if np.sum(valid_endo) > 0:
            endo_cv = (endo_stds[valid_endo] / endo_means[valid_endo]).median()
        else:
            endo_cv = 0.0
            
        pooled_cv = (control_cv + endo_cv) / 2
        
    except Exception:
        pooled_cv = 0.0
    
    # Helper functions for robust calculations
    def safe_cv(values):
        if len(values) == 0:
            return 0.0
        std_val = values.std()
        mean_val = values.mean()
        if np.abs(mean_val) < 1e-10:
            return 0.0
        return std_val / np.abs(mean_val)
    
    def safe_mad_cv(values):
        if len(values) == 0:
            return 0.0
        mad_val = values.std()
        mean_val = values.mean()
        if np.abs(mean_val) < 1e-10:
            return 0.0
        return mad_val / np.abs(mean_val)
    
    def safe_range_fold(values):
        if len(values) == 0:
            return 0.0
        range_val = values.max() - values.min()
        std_val = values.std()
        if std_val < 1e-10:
            return 0.0
        return range_val / std_val
    
    metrics = {
        'sample_mean_cv': safe_cv(sample_means),
        'sample_median_cv': safe_cv(sample_medians),
        'sample_mad_cv': safe_mad_cv(sample_mads),
        'mean_var_correlation': mean_var_corr if np.isfinite(mean_var_corr) else 0.0,
        'pooled_within_group_cv': pooled_cv if np.isfinite(pooled_cv) else 0.0,
        'sample_range_fold': safe_range_fold(sample_means),
        'n_samples': len(sample_means),
        'n_proteins': len(protein_means_final)
    }
    
    return metrics


def compare_normalization_methods(datasets_dict, biomarkers, metavariables):
    """
    Compare multiple normalization methods and provide recommendations.
    
    Args:
        datasets_dict (dict): Dictionary with method names as keys and dataframes as values
        biomarkers (list): List of biomarker columns
        metavariables (list): List of metadata columns
        
    Returns:
        dict: Comprehensive comparison results
    """
    results = {
        'metrics': {},
        'pca_results': {},
        'scores': {},
        'recommendation': None
    }
    
    # Calculate metrics for each method
    for method_name, data in datasets_dict.items():
        metrics = calculate_normalization_metrics(data, biomarkers)
        results['metrics'][method_name] = metrics
        
        # Perform PCA analysis
        df_pca, pca_obj, var_ratio = perform_pca_analysis(data, biomarkers, metavariables, method_name)
        results['pca_results'][method_name] = {
            'pca_data': df_pca,
            'pca_object': pca_obj,
            'explained_variance': var_ratio
        }
    
    # Score each method
    for method_name, metrics in results['metrics'].items():
        score = 0
        
        # Add penalty for high CV (want low CV)
        if np.isfinite(metrics['sample_mean_cv']):
            score += metrics['sample_mean_cv'] * 10
        
        if np.isfinite(metrics['sample_median_cv']):
            score += metrics['sample_median_cv'] * 10
        
        if np.isfinite(metrics['sample_mad_cv']):
            score += metrics['sample_mad_cv'] * 5
        
        if np.isfinite(metrics['pooled_within_group_cv']):
            score += abs(metrics['pooled_within_group_cv']) * 5
        
        # Add penalty for high mean-variance correlation
        if np.isfinite(metrics['mean_var_correlation']):
            score += abs(metrics['mean_var_correlation']) * 5
        
        # Add penalty for extreme sample ranges
        if np.isfinite(metrics['sample_range_fold']):
            score += max(0, metrics['sample_range_fold'] - 3) * 2
        
        results['scores'][method_name] = score
    
    # Determine recommendation
    valid_scores = {k: v for k, v in results['scores'].items() if np.isfinite(v) and v > 0}
    
    if len(valid_scores) > 0:
        best_method = min(valid_scores.keys(), key=lambda x: valid_scores[x])
        results['recommendation'] = best_method
    else:
        # All methods perform equivalently, choose based on interpretability
        method_preference = ["Mean Normalization", "No Normalization", "LOWESS Normalization"]
        available_methods = list(datasets_dict.keys())
        for preferred in method_preference:
            if preferred in available_methods:
                results['recommendation'] = preferred
                break
        
        if results['recommendation'] is None:
            results['recommendation'] = list(datasets_dict.keys())[0]
    
    return results


def plot_sample_distributions(datasets_dict, biomarkers, figsize=(18, 12)):
    """
    Plot sample distribution comparisons across normalization methods.
    
    Args:
        datasets_dict (dict): Dictionary with method names as keys and dataframes as values
        biomarkers (list): List of biomarker columns
        figsize (tuple): Figure size
    """
    fig, axes = plt.subplots(2, len(datasets_dict), figsize=figsize)
    
    if len(datasets_dict) == 1:
        axes = axes.reshape(2, 1)
    
    for i, (method_name, data) in enumerate(datasets_dict.items()):
        sample_means = data[biomarkers].mean(axis=1).dropna()
        sample_stds = data[biomarkers].std(axis=1).dropna()
        
        # Plot sample means
        if len(sample_means) > 0:
            mean_range = sample_means.max() - sample_means.min()
            if mean_range > 1e-10:
                n_bins_means = min(20, max(5, len(sample_means) // 10))
                axes[0, i].hist(sample_means, bins=n_bins_means, alpha=0.7, edgecolor='black')
                axes[0, i].axvline(sample_means.median(), color='red', linestyle='--', 
                                 label=f'Median: {sample_means.median():.3f}')
                axes[0, i].legend()
            else:
                axes[0, i].text(0.5, 0.5, f'All values ≈ {sample_means.iloc[0]:.3f}\n(No variation)', 
                               ha='center', va='center', transform=axes[0, i].transAxes,
                               bbox=dict(boxstyle="round,pad=0.3", facecolor="lightgray", alpha=0.7))
        
        axes[0, i].set_title(f'Sample Means\n{method_name}')
        axes[0, i].set_xlabel('Mean Log2 Intensity')
        axes[0, i].set_ylabel('Frequency')
        
        # Plot sample standard deviations
        if len(sample_stds) > 0:
            std_range = sample_stds.max() - sample_stds.min()
            if std_range > 1e-10:
                n_bins_stds = min(30, max(5, len(sample_stds) // 5))
                axes[1, i].hist(sample_stds, bins=n_bins_stds, alpha=0.7, edgecolor='black')
                axes[1, i].axvline(sample_stds.median(), color='red', linestyle='--',
                                 label=f'Median: {sample_stds.median():.3f}')
                axes[1, i].legend()
            else:
                axes[1, i].text(0.5, 0.5, f'All values ≈ {sample_stds.iloc[0]:.3f}\n(No variation)', 
                               ha='center', va='center', transform=axes[1, i].transAxes,
                               bbox=dict(boxstyle="round,pad=0.3", facecolor="lightgray", alpha=0.7))
        
        axes[1, i].set_title(f'Sample Standard Deviations\n{method_name}')
        axes[1, i].set_xlabel('Standard Deviation')
        axes[1, i].set_ylabel('Frequency')
    
    plt.tight_layout()
    return fig


def plot_pca_comparison(pca_results_dict, figsize=(18, 5)):
    """
    Plot PCA comparison across normalization methods.
    
    Args:
        pca_results_dict (dict): Dictionary with PCA results from compare_normalization_methods
        figsize (tuple): Figure size
    """
    fig, axes = plt.subplots(1, len(pca_results_dict), figsize=figsize)
    
    if len(pca_results_dict) == 1:
        axes = [axes]
    
    for i, (method_name, pca_result) in enumerate(pca_results_dict.items()):
        df_pca = pca_result['pca_data']
        var_ratio = pca_result['explained_variance']
        
        sns.scatterplot(data=df_pca, x='PC1', y='PC2', hue='Grupo', ax=axes[i])
        axes[i].set_title(f'PCA: {method_name}')
        axes[i].set_xlabel(f'PC1 ({var_ratio[0]*100:.1f}% Variance)')
        axes[i].set_ylabel(f'PC2 ({var_ratio[1]*100:.1f}% Variance)')
        
        # Update legend
        handles, labels = axes[i].get_legend_handles_labels()
        axes[i].legend(handles, ['Control', 'Endometriosis'])
    
    plt.tight_layout()
    return fig


def plot_sample_boxplots(data, biomarkers, title="Protein levels per sample", figsize=(20, 6), order_by_mean=False):
    """
    Create boxplots of protein intensities per sample, optionally ordered by mean intensity.
    
    Args:
        data (pd.DataFrame): Input data
        biomarkers (list): List of biomarker columns
        title (str): Title for the plot
        figsize (tuple): Figure size
        order_by_mean (bool): If True, order samples by ascending mean intensity. Default: False
        
    Returns:
        matplotlib.figure.Figure: The boxplot figure
    """
    fig, ax = plt.subplots(figsize=figsize)
    
    # Calculate sample order
    if order_by_mean:
        sample_means = data[biomarkers].mean(axis=1).sort_values()
        ordered_samples = sample_means.index
    else:
        ordered_samples = data.index
    
    # Prepare data for boxplot in the correct order
    # We need to create a list of data arrays, one for each sample in the desired order
    plot_data = []
    sample_labels = []
    colors = []
    
    for sample in ordered_samples:
        sample_data = data.loc[sample, biomarkers].dropna()
        if len(sample_data) > 0:  # Only include samples with data
            plot_data.append(sample_data.values)
            sample_labels.append(sample)
            colors.append('lightcoral' if data.loc[sample, 'Grupo'] == 1 else 'lightblue')
    
    # Create boxplot with proper ordering
    bp = ax.boxplot(plot_data, labels=sample_labels, patch_artist=True)
    
    # Apply colors to boxes
    for patch, color in zip(bp['boxes'], colors):
        patch.set_facecolor(color)
        patch.set_alpha(0.7)
    
    ax.set_title(title)
    
    # Set x-axis label based on ordering
    if order_by_mean:
        ax.set_xlabel('Samples (ordered by mean protein level)')
    else:
        ax.set_xlabel('Samples')
    
    ax.set_ylabel('Log2 Intensity')
    plt.xticks(rotation=90)
    
    # Add legend
    handles = [plt.Line2D([0], [0], marker='o', color='w', label='Endometriosis', markerfacecolor='lightcoral'),
               plt.Line2D([0], [0], marker='o', color='w', label='Control', markerfacecolor='lightblue')]
    plt.legend(handles=handles)
    
    return fig


def plot_intensity_vs_detection(data, biomarkers, title="Mean Intensity vs. Number of Proteins Detected", figsize=(10, 6)):
    """
    Create scatterplot of mean intensity vs number of proteins detected per sample.
    
    Args:
        data (pd.DataFrame): Input data
        biomarkers (list): List of biomarker columns
        title (str): Title for the plot
        figsize (tuple): Figure size
        
    Returns:
        matplotlib.figure.Figure: The scatterplot figure
    """
    fig, ax = plt.subplots(figsize=figsize)
    
    # Calculate metrics for each sample
    mean_intensities = data[biomarkers].mean(axis=1)
    num_proteins_detected = data[biomarkers].notna().sum(axis=1)
    
    # Create colors based on group
    colors = ['lightcoral' if g == 1 else 'lightblue' for g in data['Grupo']]
    
    # Create scatterplot
    scatter = ax.scatter(num_proteins_detected, mean_intensities, c=colors, alpha=0.7, s=50)
    ax.set_title(title)
    ax.set_xlabel('Number of Proteins Detected')
    ax.set_ylabel('Mean Log2 Intensity')
    
    # Add legend
    handles = [plt.Line2D([0], [0], marker='o', color='w', label='Endometriosis', markerfacecolor='lightcoral'),
               plt.Line2D([0], [0], marker='o', color='w', label='Control', markerfacecolor='lightblue')]
    plt.legend(handles=handles)
    
    # Add grid for better readability
    ax.grid(True, alpha=0.3)
    
    return fig


def plot_normalization_comparison_detailed(datasets_dict, biomarkers, figsize=(20, 15), order_by_mean=True):
    """
    Create comprehensive comparison plots showing boxplots and scatterplots for each normalization method.
    
    Args:
        datasets_dict (dict): Dictionary with method names as keys and dataframes as values
        biomarkers (list): List of biomarker columns
        figsize (tuple): Figure size
        order_by_mean (bool): If True, order samples by ascending mean intensity in boxplots. Default: True
        
    Returns:
        matplotlib.figure.Figure: The comparison figure
    """
    n_methods = len(datasets_dict)
    fig, axes = plt.subplots(2, n_methods, figsize=figsize)
    
    if n_methods == 1:
        axes = axes.reshape(2, 1)
    
    for i, (method_name, data) in enumerate(datasets_dict.items()):
        # Boxplots in top row
        if order_by_mean:
            sample_means = data[biomarkers].mean(axis=1).sort_values()
            ordered_samples = sample_means.index
            xlabel_boxplot = 'Samples (ordered by mean)'
        else:
            ordered_samples = data.index
            xlabel_boxplot = 'Samples'
            
        colors = ['lightcoral' if g == 1 else 'lightblue' for g in data.loc[ordered_samples, 'Grupo']]
        
        sns.boxplot(data=data[biomarkers].loc[ordered_samples].T, ax=axes[0, i], palette=colors)
        axes[0, i].set_title(f'Sample Boxplots\n{method_name}')
        axes[0, i].set_xlabel(xlabel_boxplot)
        axes[0, i].set_ylabel('Log2 Intensity')
        axes[0, i].tick_params(axis='x', rotation=90, labelsize=6)
        
        # Scatterplots in bottom row
        mean_intensities = data[biomarkers].mean(axis=1)
        num_proteins_detected = data[biomarkers].notna().sum(axis=1)
        colors_scatter = ['lightcoral' if g == 1 else 'lightblue' for g in data['Grupo']]
        
        axes[1, i].scatter(num_proteins_detected, mean_intensities, c=colors_scatter, alpha=0.7, s=30)
        axes[1, i].set_title(f'Intensity vs Detection\n{method_name}')
        axes[1, i].set_xlabel('Number of Proteins Detected')
        axes[1, i].set_ylabel('Mean Log2 Intensity')
        axes[1, i].grid(True, alpha=0.3)
    
    # Add overall legend
    handles = [plt.Line2D([0], [0], marker='o', color='w', label='Endometriosis', markerfacecolor='lightcoral'),
               plt.Line2D([0], [0], marker='o', color='w', label='Control', markerfacecolor='lightblue')]
    fig.legend(handles=handles, loc='upper right', bbox_to_anchor=(0.98, 0.98))
    
    plt.tight_layout()
    return fig
