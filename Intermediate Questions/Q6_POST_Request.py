#Q6. POST Request: Simulate submitting a form to https://example.com/login with JSON data { "username": "user123", "password": "pass123" }.

import requests
url = "https://httpbin.org/post"

data = {
    "username": "user123",
    "password": "pass123"
}

r = requests.post(url, json=data)
print(r.json())
