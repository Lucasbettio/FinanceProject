from aiohttp import web
from src.controller.FIIsController import FIIsController

fiis_controller = FIIsController()

async def _status():
    return web.Response(text="Ações healthy and working")

def fiis_routes(prefix):
    return[
        web.post(prefix + '/top5/fiis', fiis_controller.get_top5_fiis),
    ]