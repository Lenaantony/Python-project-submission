import requests
from bs4 import BeautifulSoup


def get_bbc_news():
    response = requests.get("https://www.bbc.com/news")
    soup = BeautifulSoup(response.text, "html.parser")

    headlines = soup.find_all("h2", attrs={"data-testid": "card-headline"})
    news_items = []

    for headline in headlines[:5]:
        title = headline.get_text()
        link_tag = headline.find_parent("a")

        if link_tag:
            link = "https://www.bbc.com" + link_tag["href"]

            time_tag = link_tag.find(
                "span",
                attrs={"data-testid": "card-metadata-lastupdated"}
            )

            news_time = time_tag.get_text() if time_tag else "No time found"

            news_items.append({
                "title": title,
                "link": link,
                "time": news_time,
                "source": "BBC"
            })

    return news_items


def get_guardian_news():
    response = requests.get("https://www.theguardian.com/international")
    soup = BeautifulSoup(response.text, "html.parser")

    links = soup.find_all("a", attrs={"aria-label": True})

    news_items = []

    for item in links[:5]:
        title = item.get("aria-label")
        href = item.get("href")

        if not title or not href:
            continue

        link = "https://www.theguardian.com" + href

        news_items.append({
            "title": title,
            "link": link,
            "time": "N/A",
            "source": "Guardian"
        })

    return news_items




bbc_news = get_bbc_news()
guardian_news = get_guardian_news()

all_news = bbc_news + guardian_news

html = """
<html>
<body>
    <h1>Daily News Digest</h1>
"""

for article in all_news:
    html += f"""
    <h2>{article['title']}</h2>
    <p>Source: {article['source']}</p>
    <p>Time: {article['time']}</p>
    <a href="{article['link']}">Read Article</a>
    <hr>
    """

html += """
</body>
</html>
"""

with open("news.html", "w", encoding="utf-8") as file:
    file.write(html)

print("news.html created")
print("Total articles:", len(all_news))