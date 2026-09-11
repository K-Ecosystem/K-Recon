import requests
from bs4 import BeautifulSoup


def extract_social_links(source_code):
    soup = BeautifulSoup(source_code, "html.parser")

    social_links = {
        "facebook": [],
        "twitter": [],
        "instagram": [],
        "youtube": [],
        "google_p": [],
        "pinterest": [],
        "github": [],
    }

    total_social_link_count = 0

    # Search patterns
    platforms = [
        ("facebook.com/", "facebook"),
        ("twitter.com/", "twitter"),
        ("instagram.com/", "instagram"),
        ("youtube.com/", "youtube"),
        ("plus.google.com/", "google_p"),
        ("github.com/", "github"),
        ("pinterest.com/", "pinterest"),
    ]

    # Find all <a> tags with an 'href' attribute
    for a_tag in soup.find_all("a", href=True):
        link = a_tag["href"]

        for domain, key in platforms:
            if domain in link:
                social_links[key].append(link)
                total_social_link_count += 1
                break  # Stop checking other platforms once matched

    return {
        "total_count": total_social_link_count,
        "social_links": social_links,
    }

def test_site(url):
    # Ensure scheme prefix exists
    if not url.startswith(("http://", "https://")):
        url = f"https://{url}"

    # Standard browser header prevents HTTP 403 access blocks
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()

        data = extract_social_links(response.text)

        print(f"=== Testing: {url} ===")
        print(f"Total Social Links Found: {data['total_count']}\n")

        for platform, links in data["social_links"].items():
            if links:
                print(f"[{platform.upper()}]")
                for link in set(links):  # Dedup for clean display
                    print(f"  -> {link}")
        print("\n" + "-" * 40 + "\n")

    except requests.RequestException as e:
        print(f"Could not fetch {url}: {e}\n")


if __name__ == "__main__":
    # Test on target websites known to have social icons/links
    targets = ["python.org", "github.com"]

    for target in targets:
        test_site(target)