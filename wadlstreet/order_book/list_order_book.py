from collections import defaultdict
from base_order_book import OrderBook

class DictionaryOrderBook(OrderBook):
    def __init__(self):
        self.bids = defaultdict(list)
        self.asks = defaultdict(list)
    
    def add_order(self, order):
        if order.side == "buy":
            self.bids[order.price].append(order)
        else:
            self.asks[order.price].append(order)
        self.match_orders()
    
    def match_orders(self):
        # Convert keys to sorted lists
        sorted_bids = sorted(self.bids.keys(), reverse=True)
        sorted_asks = sorted(self.asks.keys())

        while sorted_bids and sorted_asks and sorted_bids[0] >= sorted_asks[0]:
            best_bid_price = sorted_bids[0]
            best_ask_price = sorted_asks[0]

            bid_order = self.bids[best_bid_price][0]
            ask_order = self.asks[best_ask_price][0]
            trade_quantity = min(bid_order.quantity, ask_order.quantity)

            print(f"DictionaryOrderBook Trade executed: Price={best_ask_price}, Quantity={trade_quantity}")

            bid_order.quantity -= trade_quantity
            ask_order.quantity -= trade_quantity

            # Remove empty orders
            if bid_order.quantity == 0:
                self.bids[best_bid_price].pop(0)
                if not self.bids[best_bid_price]:
                    del self.bids[best_bid_price]
            if ask_order.quantity == 0:
                self.asks[best_ask_price].pop(0)
                if not self.asks[best_ask_price]:
                    del self.asks[best_ask_price]

            sorted_bids = sorted(self.bids.keys(), reverse=True)
            sorted_asks = sorted(self.asks.keys())

    def get_best_bid(self):
        if not self.bids:
            return None
        return max(self.bids.keys())

    def get_best_ask(self):
        if not self.asks:
            return None
        return min(self.asks.keys())
