import logging as log
from aiohttp import web
from src.services.FIIsService import FIIsService


class FIIsController(FIIsService):
    async def get_top5_fiis(self, request):
        try:
            top5_fiis = self.service_get_top_5_fiis()

            return web.json_response(top5_fiis)

        except Exception as ex:
            log.error(f"Error: {ex}")
            raise web.HTTPBadRequest(text=str(ex))
