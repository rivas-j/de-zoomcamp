

python ingest_data.py
    --user = root \
    --password = root \
    --host = localhost \
    --port = 5431 \
    --db = ny_taxi \
    --table_name = yellow_taxi_data \
    --url = 'https://drive.google.com/uc?export=download&id=17Dsiw4qoHWH4UVpXEBCi8Nhc6u4lujRS' \
    --csv_name = 'output.csv' \


URL="https://drive.google.com/uc?export=download&id=17Dsiw4qoHWH4UVpXEBCi8Nhc6u4lujRS" python ingest_data.py    --user=root\    --password=root\    --host=localhost\    --port=5431\    --db=ny_taxi\    --table_name=yellow_taxi_data\    --url=${URL}\


python ingest_data.py    --user=root   --password=root --host=localhost --port=5431 --db=ny_taxi --table_name=yellow_taxi_data --url="https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2021-01.parquet"