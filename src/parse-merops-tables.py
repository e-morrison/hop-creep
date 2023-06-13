#!/usr/bin/python

import vaex
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
import re
import os
from pathlib import Path


def open_file(sql_file):
    with open(f'data/merops/{sql_file}', 'r') as file:
        return file.read()

def save_parquet(list_in, file_name_out):
    '''
    Takes a list and saves it as a parquet file. 
    '''
    df = pd.DataFrame(list_in)
    table = pa.Table.from_pandas(df)
    pq.write_table(table, file_name_out)



def extract_values(insert_statements):
    '''
    Take INSERT INTO statements and pull the data into an empty list.
    '''

    # Initialize empty list
    data = []

    # Parse each INSERT INTO statement and extract the values
    for statement in insert_statements:
        values = re.findall(r'\((.*?)\)', statement)
        data.extend([v.strip("'") for v in value.split(',')] for value in values)
    return data


def extract_column_headers(create_table_statements):
    '''
    This will extract the column headers from the .sql file.
    '''

    # Initialize empty list
    column_headers = []

    # Parse each CREATE TABLE statement and extract the values
    for statement in create_table_statements:
        values = re.findall(r'`([^`]+)`', statement)
        column_headers.extend(values)

    return column_headers


def gen_file_out_name(sql_file):
    file_path = Path(sql_file)
    new_path = Path(file_path.name)
    return 'data/merops_parsed/' + str(new_path.with_suffix('.parquet'))




def parse_merops_sql(sql_file):
    '''
    This function parses an sql file from MEROPS and converts
    it to a pandas dataframe.
    '''

    # Open the file 
    sql_script = open_file(sql_file)

    # Extract all INSERT INTO statements from .sql file
    insert_statements = re.findall(r'INSERT INTO.*?;', sql_script, re.DOTALL)
    create_table_statements = re.findall(r'CREATE TABLE.*?;', sql_script, re.DOTALL)

    # Extract values into a data list
    data = extract_values(insert_statements)

    # Extract column headers
    column_headers = extract_column_headers(create_table_statements)

    return data, column_headers


if __name__ == "__main__":
    sql_files = [
                'cleavage.sql',
                ]

    for sql_file in sql_files:
        data, column_headers = parse_merops_sql(sql_file)

        # Check if MEROPS parsed path exists and, if not, create it
        os.makedirs('data/merops_parsed', exist_ok=True)

        # Generate new file name for parsed file
        file_name_out = gen_file_out_name(sql_file)

        # Save parsed data as a .parquet file
        data.insert(0, column_headers)
        print(file_name_out)
        save_parquet(data, file_name_out)

