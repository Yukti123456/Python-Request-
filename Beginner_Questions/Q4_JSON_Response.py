#Q4.JSON Response: Fetch data from https://jsonplaceholder.typicode.com/posts/1 and extract the title from the JSON response.

import requests

url = "https://jsonplaceholder.typicode.com/posts/1"
r = requests.get(url)
data = r.json()
print("Title: ",data["title"])
