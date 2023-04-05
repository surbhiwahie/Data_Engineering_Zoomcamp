import pandas as pd
from sqlalchemy import create_engine
import psycopg2 
from time import time

engine = create_engine('postgresql://postgres:postgres@localhost:5431/ny_taxi')

csv_name = '/Users/scarstruck/Documents/User_Surbhi/Data/yellow_tripdata_2021-01.csv'
table_name = 'yellow_taxi_data'

df_iter = pd.read_csv(csv_name, chunksize=100000)
df = next(df_iter)


while True:

    df = next(df_iter)

    df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
    df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)
    df.to_sql(name=table_name, con=engine, if_exists="append")

    print("data insertion completed.")