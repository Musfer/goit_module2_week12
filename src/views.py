import aiohttp_jinja2
import aiohttp.web
from src.search import ukr_pravda, uamap


@aiohttp_jinja2.template('index.html')
async def index(request):
    return {}


@aiohttp_jinja2.template('ukr_pravda_source.html')
async def source_pravda(request):
    return {}


@aiohttp_jinja2.template('liveuamap_source.html')
async def source_liveuamap(request):
    return {}


async def urk_pravda_news(request):
    news = await ukr_pravda.news()
    return aiohttp.web.HTTPFound(location=request.app.router['index'].url_for(news=news))


@aiohttp_jinja2.template('index.html')
async def update_up(request):
    news = await ukr_pravda.news()
    return {"news_up": news}


@aiohttp_jinja2.template('index.html')
async def update_lum(request):
    news = await uamap.news()
    return {"news_lum": news}


# async def read_word(request):
#     data = await request.post()
#     word = data["word"].strip().replace(" ", "+")
#     if not word:
#         word = "1"
#     return aiohttp.web.HTTPFound(location=request.app.router['index'].url_for(key_word=word))
