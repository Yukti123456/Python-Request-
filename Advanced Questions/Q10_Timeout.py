#Q10. Timeouts :Configure a timeout of 2 seconds for a request to https://example.com. What happens if the server doesn't respond in time?

import requests

url = "https://httpbin.org/delay/2"
try:
    r = requests.get(url, timeout=2)
    print(r.status_code)

except requests.exceptions.Timeout:
    print("Request timed out")
