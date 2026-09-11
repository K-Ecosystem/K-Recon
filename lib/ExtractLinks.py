import requests
import urllib3
from bs4 import BeautifulSoup

# Suppress SSL certificate warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def extract_links(real_link):
    # Ensure scheme prefix exists for requests
    if not real_link.startswith(("http://", "https://")):
        real_link = f"https://{real_link}"

    # Extract base domain string to check internal vs external links
    clean_domain = (
        real_link.replace("https://", "")
        .replace("http://", "")
        .replace("www.", "")
    )

    try:
        response = requests.get(real_link, verify=False, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")

        internal_links = []
        external_links = []

        # Find all <a> tags with an href attribute
        for a_tag in soup.find_all("a", href=True):
            href = a_tag["href"]
            if clean_domain in href:
                internal_links.append(href)
            else:
                external_links.append(href)

        return {
            "total_count": len(internal_links) + len(external_links),
            "internal_links": internal_links,
            "external_links": external_links,
        }

    except requests.RequestException:
        return {"total_count": 0, "internal_links": [], "external_links": []}

"""
if __name__ == "__main__":
    targets = ["www.google.com", "wikipedia.org"]

    for target in targets:
        print(f"\n--- Testing {target} ---")
        data = extract_links(target)
        print(data)
        print(f"Total Links Found : {data['total_count']}")
        print(f"Internal Links    : {len(data['internal_links'])}")
        print(f"External Links    : {len(data['external_links'])}")

        # Print sample links if available
        if data["external_links"]:
            print(f"Sample External   : {data['external_links'][0]}")
"""