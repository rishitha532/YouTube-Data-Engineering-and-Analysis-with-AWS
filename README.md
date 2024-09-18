# YouTube Data Engineering and Analysis with AWS

## Overview
This project focuses on efficiently managing and analyzing structured and semi-structured YouTube video data, categorized by video types and trending metrics, while ensuring secure processing.

## Project Objectives
- **Data Ingestion**: Implement a system to collect data from multiple sources.
- **ETL Process**: Transform raw data into a refined, usable format.
- **Data Lake**: Establish a centralized repository to store data from various sources.
- **Scalability**: Ensure the system can handle growing data volumes as they increase over time.
- **Cloud Integration**: Leverage AWS cloud services to process large datasets beyond local machine capacity.
- **Reporting**: Develop dashboards to address the key questions and insights derived from the analysis.

## Services We Will Be Using
- **Amazon S3**: An object storage service offering unmatched scalability, data availability, security, and performance for storing and retrieving any amount of data.
- **AWS IAM**: Identity and Access Management (IAM) enables secure access control for AWS services and resources, ensuring proper permissions and security protocols.
- **Amazon QuickSight**: A cloud-native business intelligence (BI) service that offers powerful, serverless, and scalable analytics with embedded machine learning capabilities.
- **AWS Glue**: A serverless data integration tool that simplifies discovering, preparing, and merging data for analytics, machine learning, and app development.
- **AWS Lambda**: A compute service that allows you to execute code in response to events without provisioning or managing servers.
- **AWS Athena**: An interactive query service that enables users to analyze data directly in S3 using SQL without the need for data loading or managing databases.

## Dataset Used
This project utilizes a dataset from Kaggle that provides daily statistics on popular YouTube videos over several months. It includes data for up to 200 trending videos per day across different regions. Each region’s data is stored in separate files, containing information such as video title, channel title, publication date, tags, views, likes, dislikes, descriptions, and comment count. The dataset also includes a `category_id` field, unique to each region, linked to a corresponding JSON file.
https://www.kaggle.com/datasets/datasnaek/youtube-new

## Architecture Diagram
![architecture](https://github.com/user-attachments/assets/d435f426-7c0a-46ff-9cd2-029bf2d9b09d)
