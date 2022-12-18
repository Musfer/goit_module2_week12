import aiohttp
import asyncio
from bs4 import BeautifulSoup
import sys
import pathlib


async def news() -> dict:
    url = "https://www.pravda.com.ua/eng/news/"
    async with aiohttp.ClientSession() as session:
        async with session.get(url, ssl=False) as response:
            result = {}
            html = await response.text()
            path = pathlib.Path(__file__).parent.parent / "templates" / "ukr_pravda_source.html"
            with open(path, "w", encoding="utf-8") as f:
                f.write(html)
            result['html'] = html
            result['news'] = []
            result['source'] = url
            soup = BeautifulSoup(html, 'lxml')
            result['date'] = soup.find("div", class_="section_header_date").find("span").text
            today_news = soup.find("div", class_="main_content")
            articles = today_news.find_all("div", class_="article_news_list")
            last_article_hour = 24
            for article in articles:
                time = article.find("div", class_="article_time").text
                hours, minutes = time.split(":")
                if int(hours) > last_article_hour:
                    break
                else:
                    last_article_hour = int(hours)
                title = article.find("div", class_="article_header").text
                link = "https://www.pravda.com.ua/" + article.find("div", class_="article_header").find("a")["href"]
                result["news"].append({"title": title, "link": link, "time": time})
    return result


# if sys.platform == 'win32':
#     asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
# asyncio.run(news())
