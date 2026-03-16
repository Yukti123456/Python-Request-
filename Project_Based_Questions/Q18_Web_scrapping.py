#Q18_ Scraping: Extract all image URLs from https://example.com (ensure compliance with the website’s robots.txt).
import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

images = soup.find_all("img")

for img in images:
    print(img["src"])
