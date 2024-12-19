import requests
from src.models.FIIs import FIIs
from config import settings


class FIIsService():
    @staticmethod
    def service_get_top_5_fiis():
        params = {
            "type": "fund",
            "sortBy":"volume",
            "sortOrder": "desc",
            "limit": "5",
            "token": settings.API_TOKEN,
        }
        
        response = requests.get(f"{settings.API_URL}/quote/list", params=params)
        data = response.json()
        if 'stocks' not in data:
            raise ValueError("A resposta da API não contém a chave 'stocks'.")
        
        fiis = [
            FIIs(
                logo=fii["logo"],
                stock=fii["stock"],
                name=fii["name"],
                change=fii["change"],
                volume=fii["volume"],
                market_cap=fii["market_cap"],
                close=fii["close"]
            ) for fii in data['stocks']
        ]
        
        return [fii.get_top_5_dict() for fii in fiis]
        
        
        