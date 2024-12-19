import logging as log
from aiohttp import web
from src.services.AcoesService import AcoesService


class AcoesController(AcoesService):
    async def get_top5_acoes(self, request):
        try:
            top5_acoes = self.service_get_top_5_acoes()

            return web.json_response(top5_acoes)
        except Exception as ex:
            log.error(f"Error: {ex}")
            raise web.HTTPBadRequest(text=str(ex))
