import requests
import json

# List of URLs to fetch from
urls = [
    "https://httpbin.org/get",
    "https://httpbin.org/get",
    "https://httpbin.org/get"
]

# Fetch and store data from each URL
for i, url in enumerate(urls):
    # Send GET request
    response = requests.get(url)
    
    # Save response as JSON
    with open(f"data_{i+1}.json", 'w') as f:
        json.dump(response.json(), f, indent=4)
    
    print(f"Downloaded from {url} and saved to data_{i+1}.json")
