import pandas as pd
from typing import Optional


class Order:
    """
    price: float
    quantity: int
    side: str
    order_type: str
    order_id: str
    timestamp: pd.Timestamp
    expiration: pd.Timestamp
    """
    def __init__(self
                ,price: float
                ,quantity: int
                ,side: str
                ,order_type: str
                ,order_id: str
                ,timestamp: pd.Timestamp
                ,expiration: Optional[pd.Timestamp]=None):
        self.price = price
        self.quantity = quantity
        self.side = side
        self.order_type = order_type
        self.order_id = order_id
        self.timestamp = timestamp
        self.expiration = expiration
    
    def __repr__(self):
        return f"Order({self.price}, {self.quantity}, {self.side}, {self.order_type}, {self.order_id}, {self.timestamp}, {self.expiration})"

    def cancel(self):
        self.expiration = pd.Timestamp.now()
    
    def is_expired(self):
        return self.expiration <= pd.Timestamp.now()
    

# class OrderBook:
#     """
#     """
#     def __init__(self,
        
# class Trader:
#     """
#     trader_id: str
#     balance: float
#     portfolio: dict
#     """
#     def __init__(self,):
#         self

# class Trade:
#     """
#     """
#     def __init__(self,):
#         self
    
        