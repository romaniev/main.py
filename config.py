environment = "production"
api_key = ""
api_secret = ""


# The list of coin pairs you want to trade with
pair_list = [
    ("DOGE", "DOGE_USD")
]

# Sets after how many hours each task should repeat
buy_frequency = 6
rebalance_frequency = 1

# The required value deviation before the coin is rebalanced.  This is a percentage
# 0.05 = 5%
# 0.15 = 15%
rebalance_threshold = 0.03

# The USDT value that PieBot will buy for each enabled coin pair in the "Buy" task
buy_order_value = 0.50

# How much USDT do you want to keep as a reserve. This is a percentage of the total portfolio balance
# 0.05 = 5%
# 0.15 = 15%
usdt_reserve = 0.02