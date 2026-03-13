#Q7. Headers: Add a custom header User-Agent: MyApp/1.0 to a GET request to https://httpbin.org/headers and print the response.
import requests

url = "https://httpbin.org/headers"

headers = {
    "User-Agent": "MyApp/1.0"
}

r = requests.get(url, headers=headers)

print(r.json())
