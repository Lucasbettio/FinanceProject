import requests
from src.models.Acoes import Acoes
from config import settings


class AcoesService():
    @staticmethod
    def service_get_top_5_acoes():
        params = {
            "sortBy": "market_cap_basic",
            "sortOrder": "desc",
            "limit": "5",
            "token": settings.API_TOKEN,
        }
        
        response = requests.get(f"{settings.API_URL}/quote/list", params=params)
        data = response.json()
        if 'stocks' not in data:
            raise ValueError("A resposta da API não contém a chave 'stocks'.")
        
        top5_acoes = [
            Acoes(
                logo=acao["logo"],
                stock=acao['stock'],
                name=acao["name"],
                change=acao["change"],
                volume=acao["volume"],
                market_cap=acao["market_cap"],
                close=acao["close"]
            ) for acao in data['stocks']
        ]
        
        return [acao.get_top5_dict() for acao in top5_acoes]