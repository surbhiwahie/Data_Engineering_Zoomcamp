
import pandas as pd
from sqlalchemy import create_engine
import psycopg2 
from time import time
import argparse
import os


def main(params):
    user = params.user
    password = params.password
    host = params.host
    port = params.port
    db = params.db
    table_name = params.table_name
    url=params.url
    csv_name = '/Users/scarstruck/Documents/User_Surbhi/Data/yellow_tripdata_2021-01.csv'
    
    os.system(f"wget {url} -o {csv_name}")
    
    #download the csv 
    
    engine = create_engine('postgresql://postgres:postgres@localhost:5431/ny_taxi')
    
    
    ## Now we need to generate the schema:
    # print(pd.io.sql.get_schema(df, name="yellow_taxi_data"))
    # print(pd.io.sql.get_schema(df, name='yellow_taxi_data', con=engine)) 

    # We are doing this, because the file size is really big, and reading a file in 
    # one go will be difficult, so we are doing this in batches. using Iterator =TRUE
    df_iter = pd.read_csv(csv_name, terator=True, chunksize=100000)
    df = next(df_iter)

    # converting a couple of columns to datetime cols: 
    df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
    df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)
   
   
   # we are using iter because, we are putting the data into the table in chunks
    while True:
    
        df = next(df_iter)
        
        df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
        df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)
        df.to_sql(name=table_name, con=engine, if_exists="append")
        
        print("data insertion completed.")





if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Ingest CSV data to Postgres')

    parser.add_argument('user', help='user name for postgres')
    parser.add_argument('password', help='password for postgres')
    parser.add_argument('host', help='host for postgres')
    parser.add_argument('post', help='port for postgres')
    parser.add_argument('db', help='database name for postgres')
    parser.add_argument('table-name', help='name of the table where we will write the result to')
    parser.add_argument('url', help='url of the csv file')


    args = parser.parse_args() 

    main(args)