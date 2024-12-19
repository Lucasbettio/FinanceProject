

class FIIs():
    def __init__(self, logo, stock, name, change, volume, market_cap, close):
        self.logo = logo
        self.stock = stock
        self.name = name
        self.change = change
        self.volume = volume
        self.market_cap = market_cap
        self.close = close

    def to_dict(self):
        return {
            "logo": self.logo,
            "stock": self.stock,
            "name": self.name,
            "change": self.change,
            "volume": self.volume,
            "market_cap": self.market_cap,
            "close": self.close
        }
        
    def get_top_5_dict(self):
        return {
            "logo":self.logo,
            "stock": self.stock,
            "name": self.name,
            "volume": self.volume
        }