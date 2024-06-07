import sqlite3
import os 
import pandas as pd
from datahandling.change_directory import chdir_sql


chdir_sql("lukas")

connection=sqlite3.connect("bachelor.db")

cursor=connection.cursor()

def create_new_table_from_df(table_name,df):
    chdir_sql("lukas")
    #first column als primary key
    column_names=tuple(df.columns)
    column_names=column_names + ("PRIMARY KEY "+"("+column_names[0]+")",) #jetzt noch nummer 1 eig 0
    print(column_names)
    request_string=f'''
    CREATE TABLE IF NOT EXISTS {table_name} {column_names};
'''
    cursor.execute(request_string)
    connection.commit()

def insert_data(table_name,df):
    chdir_sql("lukas")
    column_names=tuple(df.columns)
    placeholders = ', '.join(['?' for _ in column_names])
    print(placeholders)
    sql = f'INSERT INTO {table_name} {column_names} VALUES ({placeholders})'
    print(sql)
    for index,row in df.iterrows():
        cursor.execute(sql,row)
    connection.commit()

def get_table(table_name):
    sql = f'SELECT * FROM {table_name}'
    cursor.execute(sql)
    rows=cursor.fetchall()
    for index,row in enumerate(rows):
        if index==0:
            ser=pd.Series(row)
            df=pd.DataFrame([ser])
            print(df)
        else: 
            ser=pd.Series(row)
            df.loc[index]=ser
    return df

def del_table(table_name):
    sql= f"DROP TABLE IF EXISTS {table_name}"
    cursor.execute(sql)
    connection.commit()

def get_table_names():
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tables=cursor.fetchall()
    for table in tables:
        print(table)

def table_info(table_name):
    cursor.execute(f"PRAGMA table_info({table_name})")
    schema_info = cursor.fetchall()
    print(schema_info)
