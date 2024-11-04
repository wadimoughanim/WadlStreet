from abc import ABC, abstractmethod

class Order: #! Filled partailly field , cancel 
    def __init__(self, order_id, price, quantity, side):
        self.order_id = order_id
        self.price = price
        self.quantity = quantity
        self.side = side  # "buy" or "sell"
        self.status = "open"

    def __repr__(self):
        return f"Order(id={self.order_id}, price={self.price}, quantity={self.quantity}, side={self.side})"
    
    def change_status(self, status):
        assert status in ["open", "filled", "partially filled", "cancelled"], "Invalid order status"
        self.status = status


class OrderBook(ABC):
    """Abstract base class for different order book implementations."""
    
    @abstractmethod
    def add_order(self, order):
        pass
    
    @abstractmethod
    def match_orders(self):
        pass
    
    @abstractmethod
    def get_best_bid(self):
        pass
    
    @abstractmethod
    def get_best_ask(self):
        pass
