import requests
from bs4 import BeautifulSoup


# --------------------------------------------------------
# BASIC INFO EXTRACTOR (title, description, favicon, canonical)
# --------------------------------------------------------
def extract_basic_info(url: str):
    response = requests.get(url, timeout=10, headers={"User-Agent": "Mozilla/5.0"})
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    title = soup.title.string if soup.title else ""

    # Meta description
    desc_tag = soup.find("meta", attrs={"name": "description"})
    description = desc_tag["content"] if desc_tag and "content" in desc_tag.attrs else ""

    # Canonical
    canonical_tag = soup.find("link", rel="canonical")
    canonical = canonical_tag["href"] if canonical_tag else ""

    # Favicon
    favicon = ""
    fav_tag = soup.find("link", rel="icon")
    if fav_tag and fav_tag.get("href"):
        favicon = fav_tag["href"]

    return {
        "url": url,
        "title": title,
        "description": description,
        "favicon": favicon,
        "canonical": canonical
    }


# --------------------------------------------------------
# LIST EXTRACTOR (simple list of text + href links)
# --------------------------------------------------------
def extract_basic_list(html: str):
    soup = BeautifulSoup(html, "html.parser")
    items = []

    # Extract first 10 links
    for a in soup.find_all("a")[:10]:
        text = a.get_text(strip=True)
        href = a.get("href")
        if text and href:
            items.append({"text": text, "href": href})

    return items
