from pycoingecko import CoinGeckoAPI


cg = CoinGeckoAPI()

data = cg.get_coins_markets("usd")


def get_market_cap(data):
    return data.get('market_cap')


data.sort(key=get_market_cap, reverse=True)

print("Symbol: ", " ", "Current Price: ", " ", "Market capitalization: ", " ", "Market rank: ")
for i in range(len(data)):
    print(data[i]["symbol"], "        ", data[i]["current_price"], "       ", data[i]["market_cap"], "                ", data[i]["market_cap_rank"])