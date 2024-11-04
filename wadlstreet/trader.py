class Trader:
    def __init__(self, trader_id):
        self.trader_id = trader_id
        self.balance = 0
        self.portfolio = {}

    def update_balance(self, amount):
        self.balance += amount

    def __repr__(self):
        return f"Trader(id={self.trader_id}, balance={self.balance}, portfolio={self.portfolio})"
    
    def trade(self, order_book):
        
    
