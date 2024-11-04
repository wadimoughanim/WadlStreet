from wadlstreet.order_book import dictionary_order_book
from utils.logger import get_logger
logger = get_logger(__name__)

class Tick:
    def __init__(self):
        self.number = 0
        self.tick_size = 1 # seconds -> maarket? 

    def next(self):
        self.number += 1


class Market: # we keep track of order book at each tick
    def __init__(self):
        self.order_book = dictionary_order_book.DictionaryOrderBook()
        self.order_book_history = {}
        self.tick = Tick()

    def run(self):
