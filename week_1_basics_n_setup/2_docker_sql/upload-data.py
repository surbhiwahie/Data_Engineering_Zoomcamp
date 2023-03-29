import pandas as pd
from sqlalchemy import create_engine
import psycopg2 

engine = create_engine('postgresql://postgres:postgres@localhost:5431/ny_taxi')

engine.connect()

# df =pd.read_csv('yellow_tripdata_2021-01.csv', nrows =100)

## Now we need to generate the schema:
# print(pd.io.sql.get_schema(df, name="yellow_taxi_data"))

# print(pd.io.sql.get_schema(df, name='yellow_taxi_data', con=engine)) 


# We are doing this, because the file size is really big, and reading a file in 
# one go will be difficult, so we are doing this in batches. using Iterator =TRUE
df_iter = pd.read_csv('yellow_tripdata_2021-01.csv', 
                 iterator=True, chunksize=100000)

#df = next(df_iter)

#print("printing the length of df_iter")
#print(len(df))

# converting a couple of columns to datetime cols: 
#df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
#df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)

# inserting the data into the table

#print('started inserting data into the dataframe')
#df.to_sql(name="yellow_taxi_data", con=engine, if_exists="replace")

#print("data insertion completed")

while True:
    
    df = next(df_iter)
    
    df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
    df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)

    df.to_sql(name="yellow_taxi_data", con=engine, if_exists="append")
    
    print("data insertion completed.")
    
    
