#Q17- Fetch the first 10 users from https://jsonplaceholder.typicode.com/users and print their names and emails.

import requests

url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url)

users = response.json()

for user in users[:10]:
    print("Name:", user["name"])
    print("Email:", user["email"])
    print()
