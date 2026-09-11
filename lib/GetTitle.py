import requests
from bs4 import BeautifulSoup

def get_title(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup.title.string.strip() if soup.title else None
    except requests.RequestException:
        return None

# print("get title of google.com :",get_title("https://www.google.com"))