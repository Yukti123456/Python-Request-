Q11_Sessions & Cookies: Create a session to persist cookies across multiple requests to: https://httpbin.org/cookies/set?name=value

import requests
session = requests.Session()

# First request: set cookie
session.get("https://httpbin.org/cookies/set?name=value")

# Second request: get cookies
response = session.get("https://httpbin.org/cookies")

print(response.json())
