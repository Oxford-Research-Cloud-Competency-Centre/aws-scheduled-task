import requests
import json
import os
import tempfile

def lambda_handler(event, context):
    # List of URLs to fetch from
    urls = [
        "https://httpbin.org/get",
        "https://httpbin.org/get",
        "https://httpbin.org/get"
    ]
    
    # Use /tmp directory for storage (Lambda's writable space)
    temp_dir = "/tmp"
    
    # Fetch and store data from each URL
    results = []
    for i, url in enumerate(urls):
        # Send GET request
        response = requests.get(url)
        
        # Save response as JSON
        file_path = f"{temp_dir}/data_{i+1}.json"
        with open(file_path, 'w') as f:
            json.dump(response.json(), f, indent=4)
        
        results.append(f"Saved to {file_path}")
    
    return {
        'statusCode': 200,
        'body': f'Downloaded {len(urls)} files: {results}'
    }