#2. Response Content: How do you access the HTML content of a response? Provide a code snippet.
import requests

response = requests.get("https://www.google.com/")
html_content = response.text
print(html_content)
