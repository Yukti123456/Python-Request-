#Q3. Check Status Code: Write code to verify if a GET request to https://api.github.com returns a 200 status code.
import requests
url = "https://api.github.com"
r = requests.get(url)
print(r.status_code)
if r.status_code == 200:
    print("Valid")
else:
    print("Invalid")
