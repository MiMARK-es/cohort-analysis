"""
EndoDx Normalization Analysis Utilities

This module contains functions to run parameterized normalization analysis
for different detection thresholds and generate comprehensive reports.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import warnings
warnings.filterwarnings('ignore')

# Import existing EndoDx utilities
from endoDx_ms_utils import (
    load_endodx_pg_matrix,
    apply_mean_normalization,
    apply_lowess_normalization,
    compare_normalization_methods,
    plot_sample_distributions,
    plot_pca_comparison,
    plot_sample_boxplots,
    plot_intensity_vs_detection,
    plot_normalization_comparison_detailed
)


def run_complete_normalization_analysis(detection_threshold, pg_matrix_path, metadata_path, 
                                      save_data=True, data_dir='../../../data/ms/endoDx'):
    """
    Run complete normalization analysis for a specific detection threshold.
    
    Parameters:
    -----------
    detection_threshold : float
        Detection threshold (e.g., 0.75 for 75%)
    pg_matrix_path : str
        Path to the protein group matrix file
    metadata_path : str
        Path to the metadata file
    save_data : bool
        Whether to save normalized datasets to files
    data_dir : str
        Directory to save normalized datasets
        
    Returns:
    --------
    dict : Complete analysis results including data, metrics, and plots
    """
    
    print(f"\n{'='*60}")
    print(f"RUNNING ANALYSIS FOR {detection_threshold*100}% DETECTION THRESHOLD")
    print(f"{'='*60}")
    
    # 1. Load raw data
    print("Loading EndoDx dataset...")
    data_raw, biomarkers_all, metavariables = load_endodx_pg_matrix(
        pg_matrix_path=pg_matrix_path,
        metadata_path=metadata_path,
        nan_thresh=None,
        log2_transform=True,
        median_normalize=False
    )
    
    print(f"Dataset loaded:")
    print(f"- Samples: {len(data_raw)}")
    print(f"- Total biomarkers: {len(biomarkers_all)}")
    print(f"- Metadata variables: {len(metavariables)}")
    print(f"- Groups: {data_raw['Grupo'].value_counts().to_dict()}")
    
    # 2. Filter biomarkers by detection threshold
    print(f"\nFiltering biomarkers with >={detection_threshold*100}% detection...")
    biomarkers_filtered, detection_stats = filter_biomarkers_by_detection(
        data_raw, biomarkers_all, detection_threshold
    )
    
    # 3. Apply normalization methods
    print(f"\nApplying normalization methods to {len(biomarkers_filtered)} filtered biomarkers...")
    
    # Check if normalized data already exists
    detection_suffix = f"_det{int(detection_threshold*100)}"
    file_prefix = f'{data_dir}/pg_matrix'
    
    files_exist = all([
        os.path.exists(f'{file_prefix}_no_normalization{detection_suffix}_20250916.csv'),
        os.path.exists(f'{file_prefix}_mean_normalization{detection_suffix}_20250916.csv'),
        os.path.exists(f'{file_prefix}_lowess_normalization{detection_suffix}_20250916.csv')
    ])
    
    if files_exist and save_data:
        print("Loading existing normalized datasets...")
        data_no_norm = pd.read_csv(f'{file_prefix}_no_normalization{detection_suffix}_20250916.csv')
        data_mean_norm = pd.read_csv(f'{file_prefix}_mean_normalization{detection_suffix}_20250916.csv')
        data_lowess_norm = pd.read_csv(f'{file_prefix}_lowess_normalization{detection_suffix}_20250916.csv')
    else:
        print("Creating normalized datasets...")
        # No normalization
        data_no_norm = data_raw[metavariables + biomarkers_filtered].copy()
        
        # Mean normalization
        data_mean_norm = apply_mean_normalization(
            data_raw[metavariables + biomarkers_filtered], biomarkers_filtered
        )
        
        # LOWESS normalization
        data_lowess_norm = apply_lowess_normalization(
            data_raw[metavariables + biomarkers_filtered], biomarkers_filtered, frac=0.6
        )
        
        # Save datasets if requested
        if save_data:
            os.makedirs(data_dir, exist_ok=True)
            datasets_to_save = {
                'no_normalization': data_no_norm,
                'mean_normalization': data_mean_norm,
                'lowess_normalization': data_lowess_norm
            }
            
            for method, df in datasets_to_save.items():
                output_path = f'{file_prefix}_{method}{detection_suffix}_20250916.csv'
                df.to_csv(output_path, index=False)
                print(f"Saved {method} dataset to {output_path}")
    
    # 4. Organize datasets for comparison
    datasets = {
        'No Normalization': data_no_norm,
        'Mean Normalization': data_mean_norm,
        'LOWESS Normalization': data_lowess_norm
    }
    
    # 5. Run comprehensive comparison
    print("Running normalization comparison...")
    comparison_results = compare_normalization_methods(datasets, biomarkers_filtered, metavariables)
    
    # 6. Compile complete results
    results = {
        'detection_threshold': detection_threshold,
        'detection_threshold_pct': detection_threshold * 100,
        'data_raw': data_raw,
        'biomarkers_all': biomarkers_all,
        'biomarkers_filtered': biomarkers_filtered,
        'metavariables': metavariables,
        'detection_stats': detection_stats,
        'datasets': datasets,
        'comparison_results': comparison_results,
        'summary_stats': {
            'n_samples': len(data_raw),
            'n_biomarkers_original': len(biomarkers_all),
            'n_biomarkers_filtered': len(biomarkers_filtered),
            'n_biomarkers_removed': len(biomarkers_all) - len(biomarkers_filtered),
            'retention_rate': len(biomarkers_filtered) / len(biomarkers_all) * 100,
            'recommended_method': comparison_results['recommendation'],
            'best_score': comparison_results['scores'][comparison_results['recommendation']]
        }
    }
    
    print(f"\nAnalysis complete for {detection_threshold*100}% threshold")
    print(f"  - Filtered biomarkers: {results['summary_stats']['n_biomarkers_filtered']}")
    print(f"  - Retention rate: {results['summary_stats']['retention_rate']:.1f}%")
    print(f"  - Recommended method: {results['summary_stats']['recommended_method']}")
    print(f"  - Quality score: {results['summary_stats']['best_score']:.3f}")
    
    return results


def filter_biomarkers_by_detection(data, biomarkers, detection_threshold=0.75):
    """
    Filter biomarkers based on detection percentage across samples.
    
    Parameters:
    -----------
    data : pd.DataFrame
        DataFrame with samples and biomarker intensities
    biomarkers : list
        List of biomarker column names
    detection_threshold : float
        Minimum percentage of samples where biomarker must be detected (not NaN)
    
    Returns:
    --------
    tuple : (filtered_biomarkers, detection_stats)
        filtered_biomarkers: list of biomarkers that meet the detection threshold
        detection_stats: DataFrame with detection statistics for all biomarkers
    """
    
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
    
    print(f"  Original biomarkers: {len(biomarkers)}")
    print(f"  Filtered biomarkers (≥{detection_threshold*100}% detection): {len(filtered_biomarkers)}")
    print(f"  Removed biomarkers: {len(biomarkers) - len(filtered_biomarkers)}")
    print(f"  Retention rate: {len(filtered_biomarkers)/len(biomarkers)*100:.1f}%")
    
    return filtered_biomarkers, detection_df


def generate_threshold_summary(threshold_results):
    """
    Generate a summary markdown string for a specific threshold analysis.
    
    Parameters:
    -----------
    threshold_results : dict
        Results dictionary from run_complete_normalization_analysis
        
    Returns:
    --------
    str : Markdown formatted summary
    """
    
    r = threshold_results  # Shorthand
    stats = r['summary_stats']
    
    summary = f"""
## Analysis Results for {stats['retention_rate']:.0f}% Detection Threshold

### Biomarker Filtering Impact
- **Original biomarkers**: {stats['n_biomarkers_original']:,}
- **Filtered biomarkers**: {stats['n_biomarkers_filtered']:,} ({stats['retention_rate']:.1f}% retention)
- **Removed biomarkers**: {stats['n_biomarkers_removed']:,} ({100-stats['retention_rate']:.1f}% removed)

### Detection Statistics
- **Mean detection percentage**: {r['detection_stats']['detection_percentage'].mean():.1f}%
- **Median detection percentage**: {r['detection_stats']['detection_percentage'].median():.1f}%
- **Detection range**: {r['detection_stats']['detection_percentage'].min():.1f}% - {r['detection_stats']['detection_percentage'].max():.1f}%

### Normalization Results
- **Recommended method**: **{stats['recommended_method']}**
- **Quality score**: {stats['best_score']:.3f} (lower is better)

#### Detailed Quality Metrics:
"""
    
    # Add detailed metrics table
    metrics_df = pd.DataFrame(r['comparison_results']['metrics']).T
    summary += "\n| Method | Sample Mean CV | Sample Median CV | Pooled Within-Group CV | Mean-Var Correlation | Sample Range Fold |\n"
    summary += "|--------|----------------|------------------|------------------------|---------------------|-------------------|\n"
    
    for method in metrics_df.index:
        metrics = metrics_df.loc[method]
        summary += f"| {method} | {metrics['sample_mean_cv']:.6f} | {metrics['sample_median_cv']:.6f} | {metrics['pooled_within_group_cv']:.3f} | {metrics['mean_var_correlation']:.3f} | {metrics['sample_range_fold']:.3f} |\n"
    
    return summary


def create_detection_comparison_plot(all_results, figsize=(15, 10)):
    """
    Create comprehensive comparison plots across all detection thresholds.
    
    Parameters:
    -----------
    all_results : list
        List of results dictionaries from different thresholds
    figsize : tuple
        Figure size for the plot
        
    Returns:
    --------
    matplotlib.figure.Figure : The created figure
    """
    
    fig, axes = plt.subplots(2, 2, figsize=figsize)
    axes = axes.flatten()
    
    # Extract data for plotting
    thresholds = [r['detection_threshold_pct'] for r in all_results]
    n_biomarkers = [r['summary_stats']['n_biomarkers_filtered'] for r in all_results]
    retention_rates = [r['summary_stats']['retention_rate'] for r in all_results]
    quality_scores = [r['summary_stats']['best_score'] for r in all_results]
    recommended_methods = [r['summary_stats']['recommended_method'] for r in all_results]
    
    # Plot 1: Number of filtered biomarkers
    axes[0].bar(thresholds, n_biomarkers, color='skyblue', alpha=0.7, edgecolor='black')
    axes[0].set_xlabel('Detection Threshold (%)')
    axes[0].set_ylabel('Number of Filtered Biomarkers')
    axes[0].set_title('Biomarkers Retained by Detection Threshold')
    axes[0].grid(True, alpha=0.3)
    
    # Add value labels
    for x, y in zip(thresholds, n_biomarkers):
        axes[0].text(x, y + max(n_biomarkers)*0.01, f'{y:,}', ha='center', va='bottom', fontweight='bold')
    
    # Plot 2: Retention rates
    axes[1].plot(thresholds, retention_rates, marker='o', linewidth=2, markersize=8, color='green')
    axes[1].set_xlabel('Detection Threshold (%)')
    axes[1].set_ylabel('Retention Rate (%)')
    axes[1].set_title('Biomarker Retention Rate vs Detection Threshold')
    axes[1].grid(True, alpha=0.3)
    
    # Add value labels
    for x, y in zip(thresholds, retention_rates):
        axes[1].text(x, y + max(retention_rates)*0.02, f'{y:.1f}%', ha='center', va='bottom', fontweight='bold')
    
    # Plot 3: Quality scores
    colors = ['lightcoral' if score > 3 else 'lightgreen' if score < 2.5 else 'yellow' for score in quality_scores]
    axes[2].bar(thresholds, quality_scores, color=colors, alpha=0.7, edgecolor='black')
    axes[2].set_xlabel('Detection Threshold (%)')
    axes[2].set_ylabel('Quality Score (Lower = Better)')
    axes[2].set_title('Normalization Quality Score by Detection Threshold')
    axes[2].grid(True, alpha=0.3)
    
    # Add value labels
    for x, y in zip(thresholds, quality_scores):
        axes[2].text(x, y + max(quality_scores)*0.01, f'{y:.3f}', ha='center', va='bottom', fontweight='bold')
    
    # Plot 4: Recommended methods
    method_counts = {}
    for method in recommended_methods:
        method_counts[method] = method_counts.get(method, 0) + 1
    
    methods = list(method_counts.keys())
    counts = list(method_counts.values())
    
    axes[3].pie(counts, labels=methods, autopct='%1.0f%%', startangle=90)
    axes[3].set_title('Recommended Normalization Methods\nAcross Detection Thresholds')
    
    plt.tight_layout()
    return fig
