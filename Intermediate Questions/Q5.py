#Q5.Query Parameters: Use requests.get() to search for "Python tutorials" on https://api.example.com/search, passing parameters q=Python tutorials and page=2.

import requests

url = "https://api.example.com/search"

params = {
    "q": "Python tutorials",
    "page": 2
}
r = requests.get(url, params=params)
print(r.text)

