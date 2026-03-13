#Q12.File Upload: Upload a local file report.pdf to https://httpbin.org/post using the files parameter.

import requests

url = "https://httpbin.org/post"

files = {
    "file": open("Repo.pdf","rb")
}

response = requests.post(url, files=files)

print(response.json())
