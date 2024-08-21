import pandas as pd

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


