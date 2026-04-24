import feedparser
from datetime import datetime

# Trusted sources for Chips & Quantum
FEEDS = {
    "Semiconductor": [
        "https://spectrum.ieee.org/rss/semiconductors/fulltext",
        "https://www.semiconductors.org/feed/",
    ],
    "Quantum": [
        "https://quantumcomputingreport.com/feed/",
        "https://thequantuminsider.com/feed/"
    ]
}

def generate_markdown():
    content = f"# 🚀 Daily Tech Pulse: {datetime.now().strftime('%B %d, %Y')}\n"
    content += "> Automated news extraction for the Semiconductor & Quantum industries.\n\n"
    
    for category, urls in FEEDS.items():
        content += f"## {category} Updates\n"
        for url in urls:
            feed = feedparser.parse(url)
            # Take the top 3 latest items from each source
            for entry in feed.entries[:3]:
                date = entry.get('published', 'Recent')
                content += f"* **[{entry.title}]({entry.link})** \n  _{date}_\n\n"
        content += "---\n"

    with open("index.md", "w", encoding="utf-8") as f:
        f.write(content)

if __name__ == "__main__":
    generate_markdown()
