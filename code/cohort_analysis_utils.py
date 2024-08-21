
import pandas as pd
import numpy as np
import os
from itertools import combinations
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
        if sensitivity > 0.95 and specificity > best_score:
            
            best_score = round(specificity, 5)
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
                    compute_auc_ci=False):
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
    '''

    models = dict()
    
    for k in range(1, max_combination_size + 1):
        for combo in combinations(cols, k):
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
                if len(combo) != 2:
                    continue
                df_copy = df_copy[df_copy[combo[1]] != 0]
                X = df_copy[combo[0]].div(df_copy[combo[1]], axis=0)
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

            # compute the AUC
            y_pred = model.predict(X)
            auc = roc_auc_score(y, y_pred)

            # compute the auc confidence interval
            if compute_auc_ci:
                auc_ci = roc_auc_score(y, y_pred, method='bootstrap', n_bootstraps=1000)
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
                             'auc_ci': round(auc_ci, 5) if auc_ci else None,
                             'sensitivity': best_sensitivity, 
                             'specificity': best_specificity, 
                             'npv': best_npv, 
                             'ppv': best_ppv,
                             'best_threshold': best_threshold
                            }

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
    # Create the scatter plot
    sns.scatterplot(data=df, x=biomarker_x, y=biomarker_y, hue=target_col)
    
    # Plot the line y = x
    plt.plot([df[biomarker_x].min(), df[biomarker_x].max()], 
             [df[biomarker_x].min(), df[biomarker_x].max()], color='red')
    
    # Perform linear regression
    slope, intercept, r_value, p_value, std_err = stats.linregress(df[biomarker_x], df[biomarker_y])
    
    # Generate regression line
    x = np.linspace(df[biomarker_x].min(), df[biomarker_x].max(), 100)
    y = slope * x + intercept
    plt.plot(x, y, color='black')
    
    # Plot the confidence interval
    plt.fill_between(x, y + std_err, y - std_err, color='black', alpha=0.2)
    
    # Show the plot
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
                                    target_col)
            
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
