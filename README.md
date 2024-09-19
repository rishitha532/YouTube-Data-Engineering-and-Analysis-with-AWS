# YouTube Data Engineering and Analysis with AWS

## Overview
This project focuses on efficiently managing and analyzing structured and semi-structured YouTube video data. It employs AWS services to build an end-to-end pipeline for data processing, transformation, and analysis, enabling real-time insights using a serverless architecture.

## Project Objectives
- **Data Ingestion**: Collect data from Kaggle and upload it to Amazon S3.
- **ETL Process**: Use AWS Glue to build a Data Catalog and automate data transformations with AWS Lambda.
- **Data Lake**: Store raw, cleaned, and transformed data in different S3 buckets.
- **Scalability**: Ensure the system scales efficiently with growing datasets.
- **Cloud Integration**: Leverage AWS services for data processing, transformation, and visualization.
- **Reporting**: Visualize data and trends with Amazon QuickSight dashboards.

## AWS Services Used
- **Amazon S3**: Primary storage for raw and cleaned datasets, and query results from AWS Athena.
- **AWS CLI**: Uploaded datasets from local storage to S3, simplifying interaction with AWS services.
- **AWS Glue Crawler**: Scanned datasets, created a Data Catalog, and stored schema information in a new database.
- **AWS Lambda**: Converted JSON and CSV files to Parquet format, performed basic data cleaning, and triggered automation on changes in S3.
- **AWS Athena**: Queried the data stored in S3 for efficient analysis without loading it into a database.
- **AWS Glue Studio**: Built an ETL pipeline to transform the data and store it in the analytical S3 bucket.
- **Amazon QuickSight**: Connected to Athena for data visualization and analysis through interactive dashboards.

## Project Flow
1. **Data Upload**: Downloaded the YouTube dataset from Kaggle and uploaded it to an Amazon S3 bucket using AWS CLI.
2. **Data Crawling**: Used AWS Glue Crawler to crawl the raw data (CSV & JSON), creating a Data Catalog in a new database.
3. **Data Cleaning**: Used AWS Lambda to convert files into Parquet format for efficient storage, with basic data cleaning.
4. **Querying**: Ensured data was ready for querying using AWS Athena, and created a new S3 bucket to store query results.
5. **Trigger Setup**: Built a trigger to automatically execute the Lambda function when updates or deletions occurred in S3.
6. **ETL Pipeline**: Used AWS Glue Studio to create an ETL pipeline, transforming the cleaned data and storing it in the final analytical bucket.
7. **Data Visualization**: Connected QuickSight to Athena and built an interactive dashboard to visualize the data.

## Dataset Used: https://www.kaggle.com/datasets/datasnaek/youtube-new

## Architecture Diagram:
![architecture](https://github.com/user-attachments/assets/c2a37e6a-6145-463b-b516-28e811d61e56)

## AWS QuickSight Dashboard:
![Youtube_Quicksight](https://github.com/user-attachments/assets/17b0d3ff-a0df-46c9-9259-9a7d7c3146bb)




