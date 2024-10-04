
import pandas as pd
import numpy as np
import os
from itertools import combinations, permutations
from sklearn.metrics import roc_auc_score, roc_curve, confusion_matrix
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

def normalize_column_names(df):
    # Normalize the columns names
    df.columns = df.columns.str.replace(' ', '_')
    df.columns = df.columns.str.replace('(', '_')
    df.columns = df.columns.str.replace(')', '_')
    df.columns = df.columns.str.replace('__', '_')
    # remove _ at the end of column names
    df.columns = [c[:-1] if c[-1] == '_' else c for c in df.columns]
    df.columns = [c[:-1] if c[-1] == ' ' else c for c in df.columns]
    # remove concentration units
    # TODO: when making the database, we should store the units somewhere
    df.columns = df.columns.str.replace('_ng/mL', '')
    df.columns = df.columns.str.replace('_mg/mL', '')

    return df

def cols_as_numbers(df, cols):
    # change the , to . in all the columns that apply IF there arent float already, and convert them to float
    for col in cols:
        try:
            if df[col].dtype == 'float64':
                continue 
            df[col] = df[col].str.strip().replace(',', '.')
            # if the value is empty, replace it with NaN
            df[col] = df[col].replace('', np.nan)
            # if the value is non-numeric, replace it with NaN
            df[col] = pd.to_numeric(df[col], errors='coerce')
            df[col] = df[col].astype(float)
        except Exception as e:
            print(f'Could not convert {col} to float')
            print(e)
    return df

def cols_as_category(df, cols):
    # To do math, change the Pathology to 0 and 1, 0 being 'Benign' and 1 being 'Endometrial cancer'
    for col, vals in cols.items():
        df[col] = df[col].map(vals)
    return df

def compute_metrics(y_true, y_pred_prob, threshold=0.5):
    y_pred = (y_pred_prob >= threshold).astype(int)
    tn, fp, fn, tp = confusion_matrix(y_true, y_pred).ravel()
    sensitivity = tp / (tp + fn) if (tp + fn) > 0 else 0
    specificity = tn / (tn + fp) if (tn + fp) > 0 else 0
    npv = tn / (tn + fn) if (tn + fn) > 0 else 0
    ppv = tp / (tp + fp) if (tp + fp) > 0 else 0
    return sensitivity, specificity, npv, ppv

def find_optimal_threshold(y_true, y_pred_prob):
    '''
    Find the optimal threshold that maximizes the specificity while keeping the sensitivity
    above 95%.

    TODO: This is a dummy function we need to implement a better way to find the optimal threshold
          or the one that is useful for us.
    '''
    thresholds = np.linspace(0, 1, 100)
    best_threshold = 0.5
    best_score = 0
    best_sensitivity = 0
    best_specificity = 0
    best_npv = 0
    best_ppv = 0
    
    for threshold in thresholds:
        sensitivity, specificity, npv, ppv = compute_metrics(y_true, y_pred_prob, threshold)
        #if sensitivity > 0.95 and specificity > best_score:
        if sensitivity + specificity > best_score:
            
            #best_score = round(specificity, 5)
            best_score = sensitivity + specificity
            best_threshold = round(threshold, 5)
            best_sensitivity = round(sensitivity, 5)
            best_specificity = round(specificity, 5)
            best_npv = round(npv, 5)
            best_ppv = round(ppv, 5)
    
    return best_threshold, best_sensitivity, best_specificity, best_npv, best_ppv

def compute_models( df, 
                    cols, 
                    max_combination_size=1, 
                    method='direct', 
                    normalizing_col = None,
                    volume_col = None,
                    volume_added = 0.5,
                    apply_log=False, 
                    avoid_same_biomarker=True,
                    target_col='Pathology',
                    compute_auc_ci=False,
                    auc_threshold=0.6,
                    ):
    '''
    Compute all the models for the combinations of the columns in the dataframe df.

    Parameters:
    df: pandas DataFrame
        The dataframe with the data to be used in the models.
    cols: list
        The list of columns to be used in the models.
    max_combination_size: int
        The maximum number of columns to be used in the combinations.
    method: str
        The method to be used in the logistic regression. It can be:
        - 'direct': use the columns as they are.
        - 'normalized': divide the columns by the column in normalizing_col.
        - 'kronmal': use the columns as they are and add the column 
                     normalizing_col as another param of the model.
        - 'undo_dilution': compute the final volume and undo the dilution.
    normalizing_col: str
        The column to be used for normalization.
    volume_col: str
        The column to be used for the volume of the sample.
    volume_added: float
        The volume added to the sample to obtain the final volume.
    apply_log: bool
        If True, apply the log to the columns.
    avoid_same_biomarker: bool
        If True, avoid the same biomarker in the combination.
    target_col: str
        The column to be used as the dependent variable.
    compute_auc_ci: bool
        If True, compute the AUC confidence interval.
    auc_threshold: float
        The threshold for the AUC to be considered in the models.
    '''

    models = dict()
    

    initial_range = max_combination_size if method == 'biomarker_ratio' else 1

    for k in range(initial_range, max_combination_size + 1):
        # When computing ratios the order matters then we use permutations
        combos = combinations(cols, k) if method != 'biomarker_ratio' else permutations(cols, k)
        for combo in combos:
            # avoid the same biomarker in the combination
            # the biomarker is in the first element when splitting by _
            if avoid_same_biomarker:
                biomarkers = [c.split('_')[0] for c in combo]
                if len(biomarkers) != len(set(biomarkers)):
                    continue

            # delete nan values from the columns in a copy of the dataframe
            df_copy = df.dropna(subset=list(combo) + [target_col])
            if normalizing_col:
                df_copy = df_copy.dropna(subset=[normalizing_col])

            if method == 'undo_dilution':
                df_copy = df_copy.dropna(subset=[volume_col])
                df_copy["Final_volume"] = df[volume_col] + volume_added
                df_copy = df_copy[df_copy[volume_col] != 0]
                X = df_copy[list(combo)] 
                X = X.multiply(df_copy[volume_col].div(df_copy['Final_volume'], axis=0), axis=0)  
            elif method == 'normalized':
                X = df_copy[list(combo)].div(df_copy[normalizing_col], axis=0)
            elif method == 'kronmal':
                X = df_copy[list(combo)+[normalizing_col]]
            elif method == 'direct':
                X = df_copy[list(combo)]
            elif method == 'biomarker_ratio':
                if len(combo) == 2:
                    df_copy = df_copy[df_copy[combo[1]] != 0]
                    X = df_copy[[combo[0]]].div(df_copy[combo[1]], axis=0)
                elif len(combo) == 3:
                    df_copy = df_copy[df_copy[combo[2]] != 0]
                    X = df_copy[[combo[0],combo[1]]].div(df_copy[combo[2]], axis=0)
                else:
                    continue
            else:
                raise ValueError('normalize should be one of {normalized, kronmal, undo_dilution, direct}')

            if apply_log:
                X = np.log(X + 1)
            y = df_copy[target_col]

            # define the dependent variable
            y = df_copy[target_col]

            # fit the logistic regression model
            try:
                model = sm.Logit(y, X).fit(disp=0)
            except Exception as e:
                print(f'Could not fit the model for biomarkers: {list(combo)}')
                print(e)
                continue
            
            try:
                # compute the AUC
                y_pred = model.predict(X)
                auc = roc_auc_score(y, y_pred)

                if auc < auc_threshold:
                    continue

                # compute the auc confidence interval
                if compute_auc_ci:
                    n_bootstraps = 1000
                    auc_values = np.zeros(n_bootstraps)
                    for i in range(n_bootstraps):
                        indices = np.random.choice(len(y_pred), len(y_pred), replace=True)
                        auc_values[i] = roc_auc_score(y.values[indices], y_pred.values[indices])
                    auc_ci = np.percentile(auc_values, [2.5, 97.5])
                else:
                    auc_ci = None

                best_threshold, best_sensitivity, best_specificity, best_npv, best_ppv = find_optimal_threshold(y, y_pred)

                # save the model
                models[combo] = {'model': model, 
                                'coef': model.params,
                                'df': df_copy, 
                                'biomarkers': list(combo),
                                'y_true': y,
                                'y_pred': y_pred,
                                'roc_values': roc_curve(y, y_pred),
                                'auc': round(auc, 5), 
                                'auc_ci': auc_ci,
                                'sensitivity': best_sensitivity, 
                                'specificity': best_specificity, 
                                'npv': best_npv, 
                                'ppv': best_ppv,
                                'best_threshold': best_threshold
                                }
            except Exception as e:
                print(f'Could not compute the AUC for biomarkers: {list(combo)}')

    return models

def plot_combo_roc_to_file(model, path):
    # ensure the path exists
    os.makedirs(os.path.dirname(path), exist_ok=True)
    
    fig, ax = plt.subplots()
    ax.plot(model['roc_values'][0], model['roc_values'][1], label=f'AUC = {model["auc"]}')
    ax.plot([0, 1], [0, 1], 'k--')
    ax.set_xlabel('False Positive Rate (1 - Specificity)')
    ax.set_ylabel('True Positive Rate (Sensitivity)')
    ax.set_title('ROC curve')
    ax.legend()
    fig.savefig(path+".png")
    plt.close(fig)

    # save all the possible thresholds, sensitivity and specificities, NPV and PPV
    with open(path+".csv", 'w') as f:
        f.write('Threshold,Sensitivity,Specificity,NPV,PPV\n')
        
        # get the roc curve for y_true and y_pred
        fpr, tpr, thresholds = model['roc_values']
        for i in range(len(thresholds)):
            sensitivity, specificity, npv, ppv = compute_metrics(model['y_true'], model['y_pred'], thresholds[i])
            f.write(f'{thresholds[i]},{sensitivity},{specificity},{npv},{ppv}\n')
        f.close()


def plot_scatter_to_file(df, x, y, hue, normalizing_col, apply_log_x, apply_log_y, folder):
    # ensure the path exists
    os.makedirs(os.path.dirname(folder), exist_ok=True)

    # delete nan values from the columns in a copy of the dataframe
    if normalizing_col is not None:
        df_copy = df.dropna(subset=[x, y, hue, normalizing_col])
    else:
        df_copy = df.dropna(subset=[x, y, hue])

    # normalize the columns
    if normalizing_col is not None:
        df_copy[x] = df_copy[x].div(df_copy[normalizing_col], axis=0)
        df_copy[y] = df_copy[y].div(df_copy[normalizing_col], axis=0)
    if apply_log_x:
        df_copy[x] = df_copy[x].apply(lambda x: np.log(x + 1))
    if apply_log_y:
        df_copy[y] = df_copy[y].apply(lambda x: np.log(x + 1))
    
    # plot the scatter with the regression line and the hue and inform the correlation 
    # coefficients for spearman and pearson
    fig, ax = plt.subplots()
    sns.regplot(x=x, y=y, data=df_copy, ax=ax, ci=None, line_kws={'color': 'red'})
    ax.set_title(f'{x} vs {y}')
    if apply_log_x:
        ax.set_xlabel(f'log({x} + 1)')
    else:
        ax.set_xlabel(x)
    if apply_log_y:
        ax.set_ylabel(f'log({y} + 1)')
    else:
        ax.set_ylabel(y)

    spearman = df_copy[[x, y]].corr(method='spearman').iloc[0, 1]
    pearson = df_copy[[x, y]].corr(method='pearson').iloc[0, 1]
    ax.text(0.05, 0.95, f'Spearman: {round(spearman, 5)}\nPearson: {round(pearson, 5)}', 
            verticalalignment='top', horizontalalignment='left', 
            transform=ax.transAxes, fontsize=10)
    
    ax.legend()
    fig.savefig(folder+f'/{x}_vs_{y}.png')
    plt.close(fig)

def plot_biomarker_correlation(df, biomarker_x, biomarker_y, target_col='Pathology'):
    import matplotlib.pyplot as plt
    import seaborn as sns
    from scipy import stats
    import numpy as np
    import pandas as pd
    import scipy

    # Set significance level
    alpha = 0.05

    # Perform normality tests
    shapiro_x = stats.shapiro(df[biomarker_x])
    shapiro_y = stats.shapiro(df[biomarker_y])

    is_normal_x = shapiro_x.pvalue > alpha
    is_normal_y = shapiro_y.pvalue > alpha

    # Decide which test to perform
    if is_normal_x and is_normal_y:
        # Paired t-test
        test_stat, test_pvalue = stats.ttest_rel(df[biomarker_x], df[biomarker_y])
        test_name = 'Paired t-test'
        # Pearson correlation
        corr_coef, corr_pval = stats.pearsonr(df[biomarker_x], df[biomarker_y])
        corr_name = 'Pearson'
    else:
        # Wilcoxon signed-rank test
        test_stat, test_pvalue = stats.wilcoxon(df[biomarker_x], df[biomarker_y])
        test_name = 'Wilcoxon test'
        # Spearman correlation
        corr_coef, corr_pval = stats.spearmanr(df[biomarker_x], df[biomarker_y])
        corr_name = 'Spearman'

    # Function to format p-values in scientific notation
    def format_pvalue(pvalue):
        return f'{pvalue:.2e}'

    # Compute Coefficient of Variation for each biomarker
    def compute_cv(series):
        return (series.std() / series.mean()) * 100

    cv_x = compute_cv(df[biomarker_x])
    cv_y = compute_cv(df[biomarker_y])

    # Interpret CV values
    def interpret_cv(cv):
        if cv < 10:
            return 'Low variability'
        elif cv < 20:
            return 'Moderate variability'
        else:
            return 'High variability'

    # Simplify 'Result' text
    def interpret_normality(pvalue):
        return 'Normal (p>{})'.format(alpha) if pvalue > alpha else 'Not normal (p≤{})'.format(alpha)

    def interpret_significance(pvalue):
        return 'Significant (p<{})'.format(alpha) if pvalue < alpha else 'Not significant (p≥{})'.format(alpha)

    # Create a summary table
    table_data = {
        'Test': [
            f'Shapiro-Wilk {biomarker_x}',
            f'Shapiro-Wilk {biomarker_y}',
            test_name,
            f'{corr_name} Correlation',
            f'CV {biomarker_x}',
            f'CV {biomarker_y}'
        ],
        'Statistic': [
            f'{shapiro_x.statistic:.4f}',
            f'{shapiro_y.statistic:.4f}',
            f'{test_stat:.4f}',
            f'{corr_coef:.4f}',
            f'{cv_x:.2f}%',
            f'{cv_y:.2f}%'
        ],
        'p-value': [
            format_pvalue(shapiro_x.pvalue),
            format_pvalue(shapiro_y.pvalue),
            format_pvalue(test_pvalue),
            format_pvalue(corr_pval),
            'N/A',
            'N/A'
        ],
        'Result': [
            interpret_normality(shapiro_x.pvalue),
            interpret_normality(shapiro_y.pvalue),
            interpret_significance(test_pvalue),
            interpret_significance(corr_pval),
            interpret_cv(cv_x),
            interpret_cv(cv_y)
        ]
    }
    summary_table = pd.DataFrame(table_data)

    # Create figure and subplots with adjusted layout
    fig = plt.figure(constrained_layout=False, figsize=(15, 6))
    gs_main = fig.add_gridspec(1, 3, width_ratios=[1.5, 1, 1.5])

    # Scatter plot (Left)
    ax0 = fig.add_subplot(gs_main[0, 0])
    sns.scatterplot(data=df, x=biomarker_x, y=biomarker_y, hue=target_col, ax=ax0)
    ax0.set_title(f'Correlation between {biomarker_x} and {biomarker_y}')

    # Plot the line y = x
    min_val = min(df[biomarker_x].min(), df[biomarker_y].min())
    max_val = max(df[biomarker_x].max(), df[biomarker_y].max())
    ax0.plot([min_val, max_val], [min_val, max_val], color='red', linestyle='--')

    # Perform linear regression
    slope, intercept, r_value, p_value, std_err = stats.linregress(df[biomarker_x], df[biomarker_y])

    # Generate regression line
    x_vals = np.linspace(min_val, max_val, 100)
    y_vals = slope * x_vals + intercept

    # Calculate confidence intervals
    n = len(df)
    t = stats.t.ppf(1 - alpha / 2, n - 2)  # two-tailed t critical value
    y_pred = intercept + slope * df[biomarker_x]
    residuals = df[biomarker_y] - y_pred
    s_err = np.sqrt(np.sum(residuals**2) / (n - 2))

    mean_x = np.mean(df[biomarker_x])
    se_line = s_err * np.sqrt(1 / n + (x_vals - mean_x)**2 / np.sum((df[biomarker_x] - mean_x)**2))
    y_upper = y_vals + t * se_line
    y_lower = y_vals - t * se_line

    # Plot regression line and confidence interval
    ax0.plot(x_vals, y_vals, color='black', label='Regression Line')
    ax0.fill_between(x_vals, y_lower, y_upper, color='gray', alpha=0.2, label=f'{int((1 - alpha) * 100)}% Confidence Interval')

    ax0.legend()

    # Set aspect ratio to square
    ax0.set_aspect('equal', adjustable='datalim')

    # Distributions (Middle column)
    gs_middle = gs_main[0, 1].subgridspec(2, 1, hspace=0.4)
    ax1 = fig.add_subplot(gs_middle[0, 0])
    sns.histplot(df[biomarker_x], kde=True, ax=ax1)
    ax1.set_title(f'Distribution of {biomarker_x}')

    ax2 = fig.add_subplot(gs_middle[1, 0])
    sns.histplot(df[biomarker_y], kde=True, ax=ax2)
    ax2.set_title(f'Distribution of {biomarker_y}')

    # Table (Right)
    ax3 = fig.add_subplot(gs_main[0, 2])
    ax3.axis('off')
    # Create the table
    table = ax3.table(cellText=summary_table.values, colLabels=summary_table.columns, loc='center')

    # Adjust table formatting
    table.auto_set_font_size(False)
    table.set_fontsize(8)
    table.scale(1, 1.2)

    # Adjust column widths
    n_rows, n_cols = summary_table.shape
    col_widths = [0.35, 0.15, 0.15, 0.35]  # Adjusted widths for columns
    for i in range(n_rows+1):  # +1 for header row
        for j in range(n_cols):
            cell = table[i, j]
            cell.set_width(col_widths[j])

            # Adjust text wrapping if needed
            if j == 3:  # 'Result' column index
                cell.get_text().set_wrap(True)

    # Adjust cell heights
    for pos, cell in table.get_celld().items():
        cell.set_height(0.1)

    # Adjust table title position
    ax3.set_title('Statistical Summary', fontweight='bold', pad=10)

    # Increase spacing between subplots
    plt.subplots_adjust(wspace=0.3)

    plt.tight_layout()
    plt.show()

def plot_biomarkers_scatterplot(
    df, biomarker_x, biomarker_y, target_col='Pathology', label_x=None, label_y=None
):
    import matplotlib.pyplot as plt
    import seaborn as sns
    from scipy import stats
    import numpy as np
    import pandas as pd

    # Use provided labels or default to biomarker names
    label_x = label_x if label_x is not None else biomarker_x
    label_y = label_y if label_y is not None else biomarker_y

    # Clean data: remove NaN and infinite values
    df_clean = df[[biomarker_x, biomarker_y, target_col]].dropna()
    df_clean = df_clean[
        np.isfinite(df_clean[biomarker_x]) & np.isfinite(df_clean[biomarker_y])
    ]

    # Map target_col values to 'Benign' and 'EC'
    mapping = {0: 'Benign', 1: 'EC'}
    df_clean['Target_Label'] = df_clean[target_col].map(mapping)

    # Set significance level
    alpha = 0.05

    # Create figure and axes with explicit size and aspect ratio
    fig, ax = plt.subplots(figsize=(8, 8))

    # Define custom colors for 'Benign' and 'EC'
    custom_palette = {'Benign': '#f789c8', 'EC': '#f41c11'}

    # Scatter plot with hue based on mapped target labels and custom colors
    sns.scatterplot(
        data=df_clean,
        x=biomarker_x,
        y=biomarker_y,
        hue='Target_Label',
        palette=custom_palette,
        s=50,      # Marker size
        alpha=0.8,  # Add transparency to markers
        ax=ax
        # Removed edgecolor parameter
    )

    # Label axes with anonymized labels
    ax.set_xlabel(label_x)
    ax.set_ylabel(label_y)
    ax.set_title(f'{label_x} vs {label_y}')

    # Calculate min and max values for axes limits and plotting lines
    x_min, x_max = df_clean[biomarker_x].min(), df_clean[biomarker_x].max()
    y_min, y_max = df_clean[biomarker_y].min(), df_clean[biomarker_y].max()

    # Add margins to the min and max values
    x_range = x_max - x_min
    y_range = y_max - y_min

    margin = 0.05  # 5% margin
    x_min_margin = x_min - margin * x_range if x_range != 0 else x_min - 1
    x_max_margin = x_max + margin * x_range if x_range != 0 else x_max + 1
    y_min_margin = y_min - margin * y_range if y_range != 0 else y_min - 1
    y_max_margin = y_max + margin * y_range if y_range != 0 else y_max + 1

    # Set axes limits with margins
    ax.set_xlim(x_min_margin, x_max_margin)
    ax.set_ylim(y_min_margin, y_max_margin)

    # Ensure aspect ratio is square
    ax.set_aspect('equal', adjustable='datalim')

    # Plot the line y = x
    min_val = min(x_min_margin, y_min_margin)
    max_val = max(x_max_margin, y_max_margin)
    ax.plot(
        [min_val, max_val],
        [min_val, max_val],
        color='#21759b',     # Changed from red to black
        linestyle='--',
        linewidth=2,
        label='y = x',
        alpha=0.5
    )

    # Perform linear regression
    slope, intercept, r_value, p_value, std_err = stats.linregress(
        df_clean[biomarker_x], df_clean[biomarker_y]
    )

    # Generate regression line
    x_vals = np.linspace(min_val, max_val, 100)
    y_vals = slope * x_vals + intercept

    # Calculate confidence intervals
    n = len(df_clean)
    t = stats.t.ppf(1 - alpha / 2, n - 2)  # two-tailed t critical value
    y_pred = intercept + slope * df_clean[biomarker_x]
    residuals = df_clean[biomarker_y] - y_pred
    s_err = np.sqrt(np.sum(residuals ** 2) / (n - 2))

    mean_x = np.mean(df_clean[biomarker_x])
    se_line = s_err * np.sqrt(
        1 / n + (x_vals - mean_x) ** 2 / np.sum((df_clean[biomarker_x] - mean_x) ** 2)
    )
    y_upper = y_vals + t * se_line
    y_lower = y_vals - t * se_line

    # Plot regression line and confidence interval
    ax.plot(
        x_vals,
        y_vals,
        color='darkgray',
        linestyle='-',
        linewidth=2,
        label='Regression Line'
    )
    ax.fill_between(
        x_vals,
        y_lower,
        y_upper,
        color='gray',
        alpha=0.2,
        label=f'{int((1 - alpha) * 100)}% Confidence Interval'
    )

    # Show legend
    ax.legend()

    # Adjust layout without changing figure size
    plt.subplots_adjust(left=0.15, right=0.95, top=0.9, bottom=0.1)

    # Display the plot
    plt.show()

def plot_aucs_with_confidence_intervals(models, method, biomarkers=None):
    aucs = []
    auc_cis = []
    models_names = []
    
    # Extract the first key from models[method]
    first_key = list(models[method].keys())[0]
    
    # Iterate over the models
    for model in models[method][first_key]:
        if biomarkers is not None and model[0] not in biomarkers:
            continue
        model_name = model[0]
        model_data = models[method][first_key][model]
        model_auc = float(model_data['auc'])
        model_auc_ci = [float(ci) for ci in model_data['auc_ci']]
        
        aucs.append(model_auc)
        auc_cis.append(model_auc_ci)
        models_names.append(model_name)
    
    auc_cis = np.array(auc_cis)
    
    # Calculate the errors
    lower_err = aucs - auc_cis[:, 0]
    upper_err = auc_cis[:, 1] - aucs
    yerr = [lower_err, upper_err]
    
    # Plot the bar chart with error bars
    plt.figure(figsize=(10, 5))
    plt.bar(models_names, aucs, yerr=yerr, capsize=5, align='center')
    plt.xticks(rotation=90)
    plt.ylabel('AUC')
    plt.title(f'AUCs with Confidence Intervals for {method} Method')
    plt.show()


def models_to_csv(models, path, append=False):
    # ensure the path exists
    os.makedirs(os.path.dirname(path), exist_ok=True)
    
    # check if path file is empty or not exists
    add_header = not os.path.exists(path)
    mode = 'a' if append else 'w'

    with open(path, mode) as f:
        # get the max lenght of model['biomarkers'] for all models 
        max_len = max([len(model['biomarkers']) for model in models.values()])
        bmk_cols = ','.join([f'Biomarker_{i+1}' for i in range(max_len)])
        if not append or add_header:
            f.write(f'{bmk_cols},AUC,Sensitivity,Specificity,NPV,PPV,Best_Threshold\n')

        for model in sorted(models.values(), key=lambda x: x['auc'], reverse=True):
            f.write(f'{",".join(model["biomarkers"])}')
            for i in range(max_len + 1 - len(model['biomarkers'])):
                f.write(',')
            f.write(f'{model["auc"]},{model["sensitivity"]},{model["specificity"]},{model["npv"]},{model["ppv"]},{model["best_threshold"]}\n')
        f.close()

results_path = lambda folder_name,method, max_biomarker_count : f'{folder_name}/{method}/max_{max_biomarker_count}'


def compute_all_models_and_save(df,
                                biomarkers,
                                target_col='Pathology',
                                normalizing_col=None,
                                volume_col=None,
                                volume_added=0.5,
                                apply_log=True,
                                avoid_same_biomarker=True,
                                methods=['direct'],
                                max_biomarker_count=1,
                                folder_name='',
                                plot_rocs=False,
                                compute_auc_ci=False,
                                auc_threshold=0.6,
                                ):

    ret_models = dict()

    for method in methods:
        for biomarkers_combo in [biomarkers]:
            num_biomarkers = len(biomarkers_combo) if len(biomarkers_combo) < max_biomarker_count else max_biomarker_count
            models = compute_models(df, 
                                    biomarkers_combo, 
                                    num_biomarkers, 
                                    method, 
                                    normalizing_col,
                                    volume_col,
                                    volume_added,
                                    apply_log, 
                                    avoid_same_biomarker,
                                    target_col,
                                    compute_auc_ci,
                                    auc_threshold,
                                    )
            
            if models == dict():
                continue

            if ret_models.get(method) is None:
                ret_models[method] = dict()
            ret_models[method]["_".join(biomarkers_combo)] = models

            models_to_csv(models, results_path(folder_name,method,num_biomarkers)+'.csv', append=method == 'biomarker_ratio')

            if plot_rocs:
                for model in models.values():
                    plot_combo_roc_to_file(model, results_path(folder_name,method,num_biomarkers)+'/rocs/'+"_".join(model['biomarkers']))
    
    return ret_models
