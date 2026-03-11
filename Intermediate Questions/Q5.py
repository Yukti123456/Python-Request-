#Q5.Query Parameters: Use requests.get() to search for "Python tutorials" on https://api.example.com/search, passing parameters q=Python tutorials and page=2.

import requests
url = "https://jsonplaceholder.typicode.com/posts/1"
r = requests.get(url)
data = r.json()
print("Title: ",data["title"])

