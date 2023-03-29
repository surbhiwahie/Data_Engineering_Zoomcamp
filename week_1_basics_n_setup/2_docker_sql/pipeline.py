import sys

import pandas as pd 

print(sys.argv)

day = sys.argv[1]


print(f'job finished successfully for day = {day}')



## Network

docker run -it \
    -e PGADMIN_DEFAULT_EMAIL="admin@admin.com" \
    -e PGADMIN_DEFAULT_PASSWORD="root" \
    -p 8080:80 \
    dpage/pgadmin4

## Network

docker network create pg-network
    
docker run -it  \
    -e POSTGRES_USER="postgres" \
    -e POSTGRES_PASSWORD="postgres" \ 
    -e POSTGRES_DB="ny_taxi" \
    -v $(pwd)/ny_taxi_postgres_data:/var/lib/postgres/data  \
    -p 5431:5432  \
    --network=pg-network \   
    --name pg-database 
    postgres:13    



docker run -it \
    -e PGADMIN_DEFAULT_EMAIL="admin@admin.com" \
    -e PGADMIN_DEFAULT_PASSWORD="root" \
    -p 8080:80 \
    --network=pg-network \
    --name pgadmin \    
    dpage/pgadmin4
