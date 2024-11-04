import matplotlib.pyplot as plt

def plot_order_book(order_book):
    """Plot the order book showing volumes at each price level."""
    
    # Aggregate volume by price level for bids and asks
    bid_prices = {}
    ask_prices = {}
    
    for price, orders in order_book.bids.items():
        bid_prices[price] = sum(order.quantity for order in orders)
    
    for price, orders in order_book.asks.items():
        ask_prices[price] = sum(order.quantity for order in orders)
    
    # Sort prices and volumes for plotting
    bid_prices = dict(sorted(bid_prices.items(), reverse=True))
    ask_prices = dict(sorted(ask_prices.items()))
    
    bid_volumes = list(bid_prices.values())
    ask_volumes = list(ask_prices.values())
    
    # Plotting
    plt.figure(figsize=(10, 6))
    plt.bar(bid_prices.keys(), bid_volumes, color="blue", label="Bids", width=0.5)
    plt.bar(ask_prices.keys(), ask_volumes, color="red", label="Asks", width=0.5)

    # Customizing the plot
    plt.xlabel("Price")
    plt.ylabel("Volume")
    plt.title("Order Book Volume by Price Level")
    plt.legend()
    plt.grid(True)
    plt.show()
