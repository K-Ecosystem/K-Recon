import requests
import urllib3

# Suppress SSL certificate warnings (matches stream_context_set_default in PHP)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def web_server(urlws):
    try:
        # Send HTTP GET request with SSL verification disabled
        response = requests.get(urlws, verify=False, timeout=10)
        # Extract 'Server' header (case-insensitive in requests)
        ws = response.headers.get('Server', '')
    except requests.RequestException:
        ws = ''

    if not ws:
        
        return False
    else:
        
        return ws

# print("Testing Cloudflare.com: ", web_server("https://cloudflare.com"))