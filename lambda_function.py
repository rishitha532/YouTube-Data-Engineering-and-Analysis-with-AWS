import json
import awswrangler as wr
import pandas as pd
import urllib.parse
import os
import boto3

# Fetch environment variables
os_input_s3_cleansed_layer = os.environ['s3_cleansed_layer']
os_input_glue_catalog_db_name = os.environ['glue_catalog_db_name']
os_input_glue_catalog_table_name = os.environ['glue_catalog_table_name']
os_input_write_data_operation = os.environ['write_data_operation']

def lambda_handler(event, context):
    print("Debug: Lambda function execution started")

    # Log the received event for debugging
    print("Received event: " + json.dumps(event))

    # Extract bucket and key from the event
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')
    print(f'Bucket: {bucket}, Key: {key}')

    # Ensure Glue database exists
    glue_client = boto3.client('glue')
    try:
        glue_client.get_database(Name=os_input_glue_catalog_db_name)
    except glue_client.exceptions.EntityNotFoundException:
        glue_client.create_database(
            DatabaseInput={
                'Name': os_input_glue_catalog_db_name,
                'Description': 'Database for cleaned YouTube data'
            }
        )

    try:
        # Reading JSON file from S3 into a DataFrame
        print(f'Reading JSON file from s3://{bucket}/{key}')
        df_raw = wr.s3.read_json(f's3://{bucket}/{key}')
        print("Raw DataFrame: ", df_raw.head())

        # Normalize the JSON data
        print('Normalizing JSON data')
        df_step_1 = pd.json_normalize(df_raw['items'])
        print("Normalized DataFrame: ", df_step_1.head())

        # Write DataFrame to S3 as Parquet and update Glue Catalog
        print(f'Writing DataFrame to S3 at {os_input_s3_cleansed_layer}')
        wr_response = wr.s3.to_parquet(
            df=df_step_1,
            path=os_input_s3_cleansed_layer,
            dataset=True,
            database=os_input_glue_catalog_db_name,
            table=os_input_glue_catalog_table_name,
            mode=os_input_write_data_operation
        )

        print("wr.s3.to_parquet response: ", wr_response)
        
        return {
            'statusCode': 200,
            'body': json.dumps('Data processed successfully!')
        }

    except Exception as e:
        print(e)
        print(f'Error processing object {key} from bucket {bucket}. Ensure they exist and your bucket is in the same region as this function.')
        raise e
