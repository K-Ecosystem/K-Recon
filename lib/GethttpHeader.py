import requests

def get_http_header(real_link):
    try:
        response = requests.get(real_link, timeout=10)
        return response.headers  # Preserves CaseInsensitiveDict
    except requests.RequestException:
        return {}

# Example usage:
headers = get_http_header("https://www.google.com/")
# print(headers.get("server"))  # Output: gws
"""
for key, value in headers.items():
    print(f"({key}) : {value}")
"""