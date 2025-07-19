import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    print(f"Scraping: {url}")
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.text
    else:
        return f"Failed to fetch page: {response.status_code}"
