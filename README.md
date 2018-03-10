# binance-console
simple and easy to use console engine for fast trading on binance

Install
-------
1. You need installation of Python 3
2. Install ccxt (nice library for many crypto exchange apis) via pip3: sudo pip3 install ccxt

Usage
------
1. Edit api_key.txt and insert your <api_key> and <api_secret> to be able to use binance api 
   (you have to create an api key on binance in your account settings first)
2. Start script: python3 binance-console.py
3. You will be asked which pair you want to trade
4. Choose one of the featured options
5. Be successfull and don't loose money!

Features
--------
1. get_balances: Shows your current balances for all coins you own
2. get_open_orders: Shows currently open orders
2. buy_market: buys <amount> of <pair> for current market price
3. sell_market: sells <amount> of <pair> for current market price
4. place_buy_order: places buy order for <amount> of <pair> with limit <price>
5. place_sell_order: places sell order for <amount> of <pair> with limit <price>
6. buy_and_sell: places buy and sell order
7. buy_trail_stop: places buy order and sell if trailing stop is reached
8. buy_take_profit: buys and sells as soon as profit is reached
  
# Use this script only if you know what you' re doing and at your own risk!
