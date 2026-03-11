# Q1-Basic GET Request: Write a Python script using requests to fetch the homepage of https://example.com and print 
the response status code.
import requests
r = requests.get("https://example.com",verify=False)
print(r.status_code)
