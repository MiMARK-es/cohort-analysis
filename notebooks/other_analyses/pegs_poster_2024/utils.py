import ptitprince as pt
import ridgeplot
import pandas as pd
import scipy.stats as stats
import scikit_posthocs as sp
import matplotlib.pyplot as plt
import seaborn as sns
import os
import matplotlib.colors as mcolors

def load_and_clean_data(file_path, sheet_name='Sheet1'):
    df = pd.read_excel(file_path, sheet_name=sheet_name)
    df_clean = df.dropna(subset=['Concentration'])
    return df_clean

def kruskal_wallis_test(df, group_col='Condition', value_col='Concentration'):
    conditions = df[group_col].unique()
    concentrations_by_condition = [df[df[group_col] == condition][value_col] for condition in conditions]
    stat, p_value = stats.kruskal(*concentrations_by_condition)
    return {'statistic': stat, 'p_value': p_value, 'significant': p_value < 0.05}

def posthoc_dunn_test(df, group_col='Condition', value_col='Concentration'):
    return sp.posthoc_dunn(df, val_col=value_col, group_col=group_col, p_adjust='bonferroni')

def posthoc_conover_test(df, group_col='Condition', value_col='Concentration'):
    return sp.posthoc_conover(df, val_col=value_col, group_col=group_col, p_adjust='bonferroni')

def plot(df, bmk, func, palette, group_col='Condition', value_col='Concentration', results_dir='results'):
    fig = plt.figure(figsize=(10, 6))
    func(x=group_col, y=value_col, data=df, palette=palette)
    plt.xticks(rotation=45)
    plt.xlabel(group_col)
    plt.ylabel(f'$log([{bmk}]/[Total Protein])$')
    plt.tight_layout()
    plt.savefig(os.path.join(results_dir, f'{bmk}_{func.__name__}.svg'), format='svg')
    plt.close(fig)

def plot_heatmap_medians(df, bmk, group_col='Condition', value_col='Concentration', results_dir='results'):
    custom_palette = sns.color_palette("husl", 256)  
    pink_to_purple_palette = custom_palette[192:256]  
    cmap = mcolors.LinearSegmentedColormap.from_list("pink_purple_husl", pink_to_purple_palette)

    median_concentrations = df.groupby('Condition')['Concentration'].median().reset_index()

    condition_order = ['Reference', '24h +PBS 4ºC', '24h -PBS 4ºC', '72h +PBS 4ºC', '72h -PBS 4ºC']
    median_concentrations['Condition'] = pd.Categorical(median_concentrations['Condition'], categories=condition_order, ordered=True)
    median_concentrations = median_concentrations.sort_values('Condition')
    
    fig = plt.figure(figsize=(8, 4))
    sns.heatmap(median_concentrations.set_index(group_col).T, annot=True, fmt='.2f', cmap=cmap)
    plt.title('Heatmap of Median Concentrations by Condition')
    plt.xlabel(group_col)
    plt.tight_layout()
    plt.savefig(os.path.join(results_dir, f'{bmk}_heatmap_medians.svg'), format='svg')
    plt.close(fig)

def plot_raincloud(df, bmk, results_dir):
    plt.figure(figsize=(10, 6))
    pt.RainCloud(x='Condition', y='Concentration', data=df, palette="husl", bw=0.2, width_viol=0.6, ax=None, orient="h", alpha=0.65)
    plt.ylabel(f'$log([{bmk}]/[Total Protein])$')
    plt.tight_layout()
    plt.savefig(os.path.join(results_dir, f'{bmk}_raincloud_plot.svg'), format='svg')
    plt.close()

