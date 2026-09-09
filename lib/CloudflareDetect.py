import requests

def cloudflare_detect(real_link):
    url_hh = f"http://api.hackertarget.com/httpheaders/?q={real_link}"
    
    try:
        response = requests.get(url_hh, timeout=10)
        result_hh = response.text
    except requests.RequestException:
        result_hh = ""

    if "cloudflare" in result_hh.lower():
        # Bright Red CLI text
        return True
    else:
        # Bright Green CLI text
        return False

# print("testing cloudflare.com :", cloudflare_detect("cloudflare.com"))