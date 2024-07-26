# DLTHUB pipeline reading files into Snowflake

## Create a Snowflake trial account

## Set up a new Snowflake database and users

Run script snowflake_create_database.sql
- modify the script and replace the password of the user LOADER
- After the script is done you will have the MANGO_DATA database, the RAW schema in this database, 
the LOADER user in Snowflake to be used by DLT

## Configure the secrets and config of DLT

cp .dlt/secrets.toml.template .dlt/secrets.toml 

In the .dlt/secrets.toml file, replace the placeholders in the credentials config
destination.snowflake.credentials="snowflake://..."



## Run the DLT pipeline
python3 pipeline.py

This pipeline will create the CAP_UTILIZATION table in the RAW schema and 
load it with the data from the ./data/fedres/FRG_G17.csv file




 