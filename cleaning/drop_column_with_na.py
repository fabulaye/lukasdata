import pandas as pd
from datahandling.change_directory import chdir_data

def drop_nan_columns(df : pd.DataFrame,max_allowed_na: float=1):
    #should I copy here?
    #bool_df=df.notna()
    na_bool=df.isna()
    for column_name in df.columns:
        na_percentage=na_bool[column_name].sum()/len(na_bool)
        if na_percentage > max_allowed_na:
            df=df.drop(columns=column_name,axis=1)
            #print(f"dropped {column_name}")
    return df
