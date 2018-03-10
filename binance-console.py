"""
03/2018
Florian Schüle <florianschuele@gmail.com>
"""
import ccxt


class engine:
    """
    Console Trading Engine

    """

    def __init__(self):
        """
        Loads api key from file and initializes instance of ccxt.binance

        """
        self.__api_key = ""
        self.__api_secret = ""
        self.exchange = ccxt.binance({"apiKey": self.__api_key,
                                      "secret": self.__api_secret,
                                      "enableRateLimit": True})
        self.pair = None

    def get_balances(self):
        """
        Shows current balances of all coins on exchange

        """
        pass

    def get_open_orders(self):
        pass

    def buy_market(self):
        pass

    def sell_market(self):
        pass

    def place_buy_order(self):
        pass

    def place_sell_order(self):
        pass

    def buy_all(self):
        pass

    def sell_all(self):
        pass

    def buy_and_sell(self):
        pass

    def buy_trail_stop(self):
        pass

    def buy_take_profit(self):
        pass

def user_interface():
    """
    Show User Interface and wait for Tasks from User

    """
    if exchange.pair == None:
        set_pair()

    # User interface
    print("What will we do?\n")
    print("1) Show Balances")
    print("2) Show Open Orders")
    print("3) Buy Market")
    print("4) Sell Market")
    print("5) Place Buy Order")
    print("6) Place Sell Order")
    print("7) Buy All")
    print("8) Sell All")
    print("9) Buy and Sell")
    print("10) Buy with Trailing Stop")
    print("11) Buy and take Profit")
    print("12) Change Asset/Currency Pair")
    print("\n")

    choice = input("Enter number...")
    switch(choice)

def set_pair():
    """
    Define Asset/Currency Pair to trade with

    """
    print("Please enter Pair to Trade: ")
    currency = input("Currency? (BTC, ETH) ")
    asset = input("Asset? ")
    pair = asset + "/" + currency
    exchange.pair = pair
    print("Pair %s will be traded now..." % pair)

def switch(choice):
    """
    Returns function which corresponds to user's choice

    """
    return {"1": exchange.get_balances(),
            "2": exchange.get_open_orders(),
            "3": exchange.buy_market(),
            "4": exchange.sell_market(),
            "5": exchange.place_buy_order(),
            "6": exchange.place_sell_order(),
            "7": exchange.buy_all(),
            "8": exchange.sell_all(),
            "9": exchange.buy_and_sell(),
            "10": exchange.buy_trail_stop(),
            "11": exchange.buy_take_profit(),
            "12": set_pair()
            }[choice]


# Start UI for trading engine
if __name__ == "__main__":
    print("##### BINANCE TRADING ENINGE STARTED #####")

    # Init Engine
    exchange = engine()

    # User Interface
    while(True):
        user_interface()




