from functions import *
import argparse
import gc
import schedule
import signal
import cryptocom.exchange as cro
import asyncio
import pandas as pd
import datetime

pre_flight_checks()

pair=("DOGE", "DOGE_USD")

increase_percentage=1+0.002

# Hard codes the minimum order value
min_order_value = 0.25
order_value=2

quantity=20


order_value = buy_order_value


##Buy###
def buy():
    if environment == "production":
        order_confirmed = False
        order = order_buy(pair[1], order_value)
        time.sleep(0.1)
    if order.status_code == 200:
        order_confirmed = True

        print_value = round(order_value, 2)
        current_time(True)
        print(str(print_value) + " USDT - " + pair[0], end=" ")
        print(colored("[BUY]", "green"))

    if not order_confirmed:
        print(order.status_code, order.reason)
        print(order.content)

    else:
        print_value = round(order_value, 2)
        current_time(True)
        print(str(print_value) + " USDT - " + pair[0], end=" ")
        print(colored("[BUY]", "green"))




###Sell
def sell():
 if environment == "production":
     order_confirmed = False

     order_request = order_sell(pair[1], quantity)
     time.sleep(0.1)
     if order_request.status_code == 200:
         order_confirmed = True
     current_time(True)
     print(colored("[SELL]", "magenta"))

     if not order_confirmed:
         print(order_request.status_code, order_request.reason)
         print(order_request.content)

     else:
         print('Order_placed')
         current_time(True)

         print(colored("[SELL]", "magenta"))



async def coin_price ():
    exchange = cro.Exchange()
    df = pd.DataFrame(columns=['token', 'value', 'time'])
    now = datetime.datetime.now()
    price = await exchange.get_price(cro.pairs.DOGE_USD)
    return price


def coin_price(pair):
    get_price_response = requests.get("https://api.crypto.com/v2/public/get-ticker?instrument_name=DOGE_USD")
    ticker = json.loads(get_price_response.content)

    price = ticker["result"]['data'][0]['b']

    return price






#buy()
c=coin_price(pair)
c=float(c)
print('Bought at')
print(c)

i=1


while i>0:
    #time.sleep(0.5)
    b = float(coin_price(pair))
    print(b)
    #d=c*increase_percentage
    d=0.071629*increase_percentage
    if b>d:
        print(d)
        sell()
        i=0
        print('Sell at')

    else:
        print('re-check')

