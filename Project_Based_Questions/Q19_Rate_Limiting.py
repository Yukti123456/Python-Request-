#Q19_Rate Limiting: Write a script to handle rate limits (retry after 429 status code) when querying: https://api.github.com.

import requests
import time

url = "https://api.github.com"

while True:
    response = requests.get(url)
  
    if response.status_code == 200:
        print("Request successful")
        print(response.json())
        break
    elif response.status_code == 429:
        print("Rate limit exceeded. Retrying after 5 seconds...")
        time.sleep(5)
    else:
        print("Request failed with status code:", response.status_code)
        break
