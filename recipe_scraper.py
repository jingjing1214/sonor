import requests
from bs4 import BeautifulSoup

def search_recipes(ingredients):
    query = f"{ingredients} 食譜 site:icook.tw"
    url = f"https://www.google.com/search?q={query}"
    headers = {"User-Agent": "Mozilla/5.0"}
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, "html.parser")
    results = []
    for g in soup.find_all("div"):
        if g.select_one("h3") and g.select_one("a"):
            title = g.select_one("h3").text
            link = g.select_one("a")["href"]
            snippet = g.get_text()
            results.append((title, link, snippet[:100]))
        if len(results) >= 5:
            break
    return results