import asyncio
import sys
import aiohttp_jinja2
import jinja2
from aiohttp import web
from src.routes import setup_routes
import pathlib

BASE_DIR = pathlib.Path(__file__).parent
app = web.Application()
aiohttp_jinja2.setup(app,
                     loader=jinja2.FileSystemLoader(str(BASE_DIR / 'src' / 'templates')))
setup_routes(app)
if sys.platform == 'win32':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
web.run_app(app)


