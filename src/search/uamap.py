import aiohttp
import asyncio
from bs4 import BeautifulSoup
import sys
import pathlib


async def news() -> dict:
    url = "https://liveuamap.com/"
    async with aiohttp.ClientSession() as session:
        async with session.get(url, ssl=False) as response:
            result = {}
            html = await response.text()
            path = pathlib.Path(__file__).parent.parent / "templates" / "liveuamap_source.html"
            with open(path, "w", encoding="utf-8") as f:
                f.write(html)
            result['html'] = html
            result['news'] = []
            result['source'] = url
            soup = BeautifulSoup(html, 'lxml')
            latest_news = soup.find_all("div", class_="event cat1 sourcees")
            for article in latest_news:
                time = article.find("span", class_="date_add").text
                link = article.find("a")["href"]
                title = article.find("div", class_="title").text
                result["news"].append({"title": title, "link": link, "time": time})
    return result


# if sys.platform == 'win32':
#     asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
# asyncio.run(news())
