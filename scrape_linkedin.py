"""
LinkedIn Post Scraper for B2B Email Marketing Research
Note: LinkedIn blocks automated scraping. This script uses requests + BeautifulSoup
as a best-effort approach. Manual collection is used as fallback where blocked.
"""

import requests
from bs4 import BeautifulSoup
import os
import time

EXPERTS = [
    {"name": "emily-kramer", "url": "https://www.linkedin.com/in/emilykramer/recent-activity/shares/"},
    {"name": "dave-gerhardt", "url": "https://www.linkedin.com/in/davegerhardt/recent-activity/shares/"},
    {"name": "samar-owais", "url": "https://www.linkedin.com/in/samarowais/recent-activity/shares/"},
    {"name": "chenell-basilio", "url": "https://www.linkedin.com/in/chenellbasilio/recent-activity/shares/"},
    {"name": "val-geisler", "url": "https://www.linkedin.com/in/valgeisler/recent-activity/shares/"},
    {"name": "corey-haines", "url": "https://www.linkedin.com/in/coreyhaines/recent-activity/shares/"},
    {"name": "jay-schwedelson", "url": "https://www.linkedin.com/in/schwedelson/recent-activity/shares/"},
    {"name": "nathan-barry", "url": "https://www.linkedin.com/in/nathanbarry/recent-activity/shares/"},
    {"name": "lenny-rachitsky", "url": "https://www.linkedin.com/in/lennyrachitsky/recent-activity/shares/"},
    {"name": "kipp-bodnar", "url": "https://www.linkedin.com/in/kippbodnar/recent-activity/shares/"},
]

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

output_dir = "research/linkedin-posts"
os.makedirs(output_dir, exist_ok=True)

for expert in EXPERTS:
    print(f"Trying: {expert['name']}...")
    try:
        response = requests.get(expert["url"], headers=HEADERS, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")
        text = soup.get_text(separator="\n", strip=True)

        with open(f"{output_dir}/{expert['name']}.md", "w", encoding="utf-8") as f:
            f.write(f"# LinkedIn Posts: {expert['name']}\n\n")
            f.write(f"Source: {expert['url']}\n\n")
            f.write("## Scraped Content\n\n")
            f.write(text[:3000])

        print(f"✓ Saved: {expert['name']}")
    except Exception as e:
        print(f"✗ Failed: {expert['name']} → {e}")
    time.sleep(2)

print("Done!")
