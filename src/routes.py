from aiohttp.web import Application
from src.views import index, source_pravda, update_up, update_lum, source_liveuamap


def setup_routes(app: Application):
    app.router.add_get('/', index, name='index')
    app.router.add_get('/source_ukr_pravda', source_pravda, name='source_pravda')
    app.router.add_get('/liveuamap_source', source_liveuamap, name='source_liveuamap')
    app.router.add_get('/updateUP', update_up, name='update_up')
    app.router.add_get('/updateLUM', update_lum, name='update_lum')


