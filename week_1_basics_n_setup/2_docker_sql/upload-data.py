#!/usr/bin/env python
# coding: utf-8

import os
import argparse
import pandas as pd
from sqlalchemy import create_engine
from time import time


def main(params):
    user = params.user
    password = params.password
    host = params.host
    port = params.port
    db = params.db
    table_name = params.table_name
    url = params.url
    csv_name = 'output.csv'

    # download the csv
    os.system(f"wget {url} -O {csv_name}")
    # df = pd.read_csv('yellow_tripdata_2021-01.csv', nrows= 100)

    df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
    df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)

    engine = create_engine('postgresql://{user}:{password}@{host}:{port}/{db}')
    
    df_iter = pd.read_csv(csv_name, iterator='true', chunksize=100000, on_bad_lines='warn', low_memory=False)
        
    df=next(df_iter)
        
    df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
    df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)
        
    
    df.to_sql(name=table_name, con=engine, if_exists='replace')
        
    for chunk in df_iter:
        t_start=time()
            
        chunk.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
        chunk.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)
        chunk.to_sql(name=table_name, con=engine, if_exists='append')
            
        t_end=time()
        print('Inserted another chunk..., took %3f seconds' % (t_end-t_start))

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Ingest CSV data to Postgres.')

    # user, 
    # password
    # host
    # port
    # database name
    # table name
    # url of the csv
    parser.add_argument('--user', help='username for postgres')
    parser.add_argument('--password', help='password for postgres')
    parser.add_argument('--host', help='host for postgres')
    parser.add_argument('--port', help='port for postgres')
    parser.add_argument('--db', help='database name for postgres')
    parser.add_argument('--table_name', help='name of th table where we will write the results to')
    parser.add_argument('--url', help='url of the csv file')

    args = parser.parse_args()
    main(args)



