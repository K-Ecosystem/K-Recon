import requests
import urllib3

# Suppress SSL certificate warnings (matches CURLOPT_SSL_VERIFYPEER = false)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def robotsdottxt(reallink):
    # Ensure link formatting and construct target URL
    rbturl = f"{reallink.rstrip('/')}/robots.txt"
    
    try:
        response = requests.get(rbturl, verify=False, timeout=10)
        
        if response.status_code == 200:
            rbtcontent = response.text
            if not rbtcontent.strip():
                return False
            else:
                return rbtcontent
        else:
            
            return False
            
    except requests.RequestException:
        return False


# print("=== Testing google.com ===", robotsdottxt("https://www.google.com"))