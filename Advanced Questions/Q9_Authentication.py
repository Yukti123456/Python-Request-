#Q9.Use HTTP Basic Auth to access a protected endpoint:https://httpbin.org/basic-auth/user/pass
import requests
    r = requests.get("https://httpbin.org/basic-auth/user/pass", auth=("user", "pass"))
    print(r.json())
    if r.status_code == 200:
         print("Authentication successful")
    else:
         print("Wrong username or password")
