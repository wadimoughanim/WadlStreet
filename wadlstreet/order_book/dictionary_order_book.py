from collections import defaultdict
from .base_order_book import OrderBook
from utils.logger import get_logger

logger = get_logger(__name__)

class DictionaryOrderBook(OrderBook):
    def __init__(self):
        logger.info("DictionaryOrderBook instance created")
        self.bids = defaultdict(list)
        self.asks = defaultdict(list)
    
    def add_order(self, order):
        if order.side == "buy":
            self.bids[order.price].append(order)
            logger.info(f"DictionaryOrderBook added bid order: {order}")
        else:
            self.asks[order.price].append(order)
            logger.info(f"DictionaryOrderBook added ask order: {order}")
        self.match_orders()
    
    def match_orders(self):
        # Sort prices for bid and ask
        sorted_bids = sorted(self.bids.keys(), reverse=True)
        sorted_asks = sorted(self.asks.keys())
        logger.info(f"Matching orders: Bids={sorted_bids}, Asks={sorted_asks}")

        while sorted_bids and sorted_asks and sorted_bids[0] >= sorted_asks[0]:
            best_bid_price = sorted_bids[0]
            best_ask_price = sorted_asks[0]

            bid_order = self.bids[best_bid_price][0]
            ask_order = self.asks[best_ask_price][0]
            trade_quantity = min(bid_order.quantity, ask_order.quantity)

            print(f"Trade executed: Price={best_ask_price}, Quantity={trade_quantity}")

            bid_order.quantity -= trade_quantity
            ask_order.quantity -= trade_quantity

            # Update order statuses
            if bid_order.quantity == 0:
                bid_order.change_status("filled")
                logger.info(f"Bid order filled: {bid_order}")
                self.bids[best_bid_price].pop(0)
                if not self.bids[best_bid_price]:
                    del self.bids[best_bid_price]
            else:
                bid_order.change_status("partially filled")
                logger.info(f"Bid order partially filled: {bid_order}")

            if ask_order.quantity == 0:
                ask_order.change_status("filled")
                logger.info(f"Ask order filled: {ask_order}")
                self.asks[best_ask_price].pop(0)
                if not self.asks[best_ask_price]:
                    del self.asks[best_ask_price]
            else:
                ask_order.change_status("partially filled")
                logger.info(f"Ask order partially filled: {ask_order}")

            # Update sorted lists in case of removal
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
