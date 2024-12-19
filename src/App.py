from aiohttp import web
from src.routes.Acoes import acoes_routes
from src.routes.FIIs import fiis_routes


class App:
    def __init__(self):
        self.app = web.Application()
        self.prefix = '/api'
        self.routes()
    
    async def _status(self):
        return web.Response(text="Healthy and working")

    def routes(self):
        self.app.add_routes([web.get(f"{self.prefix}/status", self._status)])
        self.app.add_routes(acoes_routes(self.prefix))
        self.app.add_routes(fiis_routes(self.prefix))
    
    def get_app(self):
        return self.app