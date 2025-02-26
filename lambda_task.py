import requests
import json
import os
import boto3
from datetime import datetime

def lambda_handler(event, context):
    # List of URLs to fetch from
    urls = [
        "https://httpbin.org/get",
        "https://httpbin.org/get",
        "https://httpbin.org/get"
    ]
    
    # S3 bucket name
    bucket_name = "my-lambda-data-bucket"
    
    # Initialize S3 client
    s3 = boto3.client('s3')
    
    # Check if bucket exists and create if it doesn't
    try:
        s3.head_bucket(Bucket=bucket_name)
    except s3.exceptions.ClientError as e:
        # If the bucket doesn't exist, create it
        if e.response['Error']['Code'] == '404':
            try:
                # Always specify the location constraint with the current region
                region = os.environ['AWS_REGION']
                s3.create_bucket(
                    Bucket=bucket_name,
                    CreateBucketConfiguration={
                        'LocationConstraint': region
                    }
                )
                print(f"Bucket {bucket_name} created successfully")
            except Exception as create_error:
                return {
                    'statusCode': 500,
                    'body': f'Error creating bucket: {str(create_error)}'
                }
        else:
            # If it's a different error (like permissions), return it
            return {
                'statusCode': 500,
                'body': f'Error accessing bucket: {str(e)}'
            }
    
    # Extract date from timestamp in event
    date_folder = datetime.now().strftime("%Y-%m-%d")
    
    # Create directory path with date
    directory_path = f"data/{date_folder}"
    
    # Fetch and store data from each URL
    results = []
    for i, url in enumerate(urls):
        # Send GET request
        response = requests.get(url)
        
        # Convert response to JSON
        response_data = response.json()
        
        # Create S3 key (path in bucket)
        file_key = f"{directory_path}/data_{i+1}.json"
        
        # Upload to S3
        try:
            s3.put_object(
                Bucket=bucket_name,
                Key=file_key,
                Body=json.dumps(response_data, indent=4),
                ContentType='application/json'
            )
            s3_url = f"s3://{bucket_name}/{file_key}"
            results.append(f"Saved to {s3_url}")
        except Exception as upload_error:
            results.append(f"Error saving to S3: {str(upload_error)}")
    
    return {
        'statusCode': 200,
        'body': f'Downloaded {len(urls)} files: {results}'
    }