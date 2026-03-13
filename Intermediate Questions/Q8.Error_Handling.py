#Q8. Error Handling: Write a try-except block to handle a ConnectionError when requesting an invalid URL.
import requests

url = "https://invalid-url-12345.com"

try:
    r = requests.get(url)
    print(r.text)

except requests.exceptions.ConnectionError as e:
    print("Connection failed:", e)
