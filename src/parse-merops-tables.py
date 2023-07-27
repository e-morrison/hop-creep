#!/usr/bin/python

import vaex
import os, sys, re, csv




if __name__ == "__main__":
    #parquet_files = [file1 for file1 in os.listdir('data/merops_parsed/') if file1.endswith('.parquet')]

    parquet_files = [
                    'Substrate_search.parquet',
                    'residue_codes.parquet',
                    ]

    for parquet_file in parquet_files:
        df = vaex.open(f'data/merops_parsed/{parquet_file}')
        print('')
        print(parquet_file)
        print(df)
