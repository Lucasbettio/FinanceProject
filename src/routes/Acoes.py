from aiohttp import web
from src.controller.AcoesController import AcoesController

acoes_controller = AcoesController()

async def _status():
    return web.Response(text="Ações healthy and working")

def acoes_routes(prefix):
    return[
        web.post(prefix + '/top5/acoes', acoes_controller.get_top5_acoes),
    ]