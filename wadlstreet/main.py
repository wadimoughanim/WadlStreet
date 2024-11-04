from wadlstreet.order_book import dictionary_order_book
from wadlstreet.order_book.base_order_book import Order
from wadlstreet.utils.visualization import plot_order_book

if __name__ == '__main__':
    # init orderbook
    order_book = dictionary_order_book.DictionaryOrderBook()
    # add orders
    order_book.add_order(Order(order_id=1, price=90, quantity=5, side="buy"))
    order_book.add_order(Order(order_id=2, price=100, quantity=5, side="sell"))
    order_book.add_order(Order(order_id=3, price=95, quantity=10, side="buy"))
    order_book.add_order(Order(order_id=4, price=95, quantity=5, side="sell"))
    print(order_book.bids)

    print(f"Best bid: {order_book.get_best_bid()}")
    print(f"Best ask: {order_book.get_best_ask()}")
    # plot order book
    plot_order_book(order_book)

    
    