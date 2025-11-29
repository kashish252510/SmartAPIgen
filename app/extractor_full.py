import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def extract_full_page(url: str):
    response = requests.get(url, timeout=10, headers={"User-Agent": "Mozilla/5.0"})
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")

    # Remove unwanted tags
    for tag in soup(["script", "style", "noscript"]):
        tag.extract()

    full_text = soup.get_text(separator=" ", strip=True)

    headings = {
        h: [tag.get_text(strip=True) for tag in soup.find_all(h)]
        for h in ["h1", "h2", "h3", "h4", "h5", "h6"]
    }

    links = [urljoin(url, a["href"]) for a in soup.find_all("a", href=True)]
    images = [urljoin(url, img["src"]) for img in soup.find_all("img", src=True)]

    meta = {}
    for tag in soup.find_all("meta"):
        name = tag.get("name") or tag.get("property")
        content = tag.get("content")
        if name and content:
            meta[name] = content

    canonical_tag = soup.find("link", rel="canonical")
    canonical = canonical_tag["href"] if canonical_tag else None

    return {
        "url": url,
        "title": soup.title.string if soup.title else "",
        "description": meta.get("description", ""),
        "canonical": canonical,
        "word_count": len(full_text.split()),
        "headings": headings,
        "full_text": full_text[:5000],
        "links": links,
        "images": images,
        "meta_tags": meta,
    }
