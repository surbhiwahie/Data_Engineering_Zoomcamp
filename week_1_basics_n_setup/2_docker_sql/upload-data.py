import pandas as pd
from sqlalchemy import create_engine
import psycopg2 

engine = create_engine('postgresql://postgres:postgres@localhost:5432/ny_taxi')

print("hello I am here")
df =pd.read_csv('yellow_tripdata_2021-01.csv', nrows =100)

df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)

print("I am making this new change")
print(pd.io.sql.get_schema(df, name='yellow_taxi_data', con=engine))