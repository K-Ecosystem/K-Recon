import requests
import urllib3

# Suppress SSL certificate warnings (matches PHP's verify_peer => false)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def read_contents(url_to_read):
    try:
        response = requests.get(url_to_read, verify=False, timeout=10)
        return response.text
    except requests.RequestException:
        return ""
# print("read content of google :", read_contents("https://www.google.com"))