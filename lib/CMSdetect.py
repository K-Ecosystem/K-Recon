import requests

def read_contents(url):
    try:
        response = requests.get(url, timeout=10)
        return response.text
    except requests.RequestException:
        return ""

def cms_detect(real_link):
    cmssc = read_contents(real_link)
    
    if '/wp-content/' in cmssc:
        return "WordPress"
    elif 'Joomla' in cmssc:
        return "Joomla"
    else:
        drp_url = f"{real_link}/misc/drupal.js"
        drpsc = read_contents(drp_url)
        
        if 'Drupal' in drpsc:
            return "Drupal"
        elif '/skin/frontend/' in cmssc:
            return "Magento"
        elif 'content="WordPress' in cmssc:
            return "WordPress"
        else:          
            return False

# print("cms scan joomla.org", cms_detect("https://joomla.org"))