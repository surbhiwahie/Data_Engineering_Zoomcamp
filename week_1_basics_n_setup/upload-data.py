import pandas as pd
print("hello world")
import pyarrow.parquet as pq

output_name = "https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2021-01.parquet"

parquet_file = pq.ParquetFile(output_name)
parquet_size = parquet_file.metadata.num_rows

print(parquet_size)