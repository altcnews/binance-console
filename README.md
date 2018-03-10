# binance-console
simple and easy to use console engine for fast trading on binance

Install
-------
1. You need installation of Python 3
2. Install ccxt (nice library for many crypto exchange apis) via pip3: sudo pip3 install ccxt

Usage
------
1. Edit binance-console and insert your <api_key> and <api_secret> to be able to use binance api 
   (you have to create an api key on binance in your account settings first)
2. Start script: python3 binance-console.py
3. You will be asked which pair you want to trade
4. Choose one of the featured options
5. Be successfull and don't loose money!

Features
--------
1. get_balances: Shows your current balances for all coins you own
2. get_open_orders: Shows currently open orders
3. buy_market: Buys <amount> of <pair> for current market price
4. sell_market: Sells <amount> of <pair> for current market price
5. place_buy_order: Places buy order for <amount> of <pair> with limit <price>
6. place_sell_order: Places sell order for <amount> of <pair> with limit <price>
7. buy_all: Buys <pair> with complete amount of buy-coin on your binance wallet
8. sell_all: Sells <pair> with complete amount amount of buy-coin on your binance wallet
9. buy_and_sell: Places buy and sell order
10. buy_trail_stop: Places buy order and sell if trailing stop is reached
11. buy_take_profit: Buys and sells as soon as profit is reached
12. change_pair: Changes Currency/Asset pair
  
  
Use this script only if you know what you' re doing and at your own risk!
--------
