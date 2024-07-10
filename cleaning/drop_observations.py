import pandas as pd
from datahandling.change_directory import chdir_sql_requests

def drop_observations(dataframe_path,column,min_count,output_name):
    chdir_sql_requests()
    df=pd.read_csv(dataframe_path)
    company_counts = df[column].value_counts()
    companies_to_keep = company_counts[company_counts >= min_count].index
    df_filtered = df[df[column].isin(companies_to_keep)]
    df_filtered.to_csv(output_name)
    return df_filtered






