import ptitprince as pt
import ridgeplot
import pandas as pd
import scipy.stats as stats
import scikit_posthocs as sp
import matplotlib.pyplot as plt
import seaborn as sns
import os
import matplotlib.colors as mcolors
from scipy.stats import shapiro, kruskal

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

def shapiro_wilk_test(df, value_col, group_col):
    shapiro_results = {}
    for condition in df[group_col].unique():
        condition_data = df[df[group_col] == condition][value_col]
        stat, p_value = shapiro(condition_data)
        shapiro_results[condition] = {'Statistic': stat, 'p-value': p_value, 'Normal': p_value > 0.05}
    return shapiro_results
