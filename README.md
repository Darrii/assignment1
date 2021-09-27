# Assignment 1

Created by Yermakhankyzy Dariga SE-2007

## Installation

Download the [python](https://www.python.org/) to install Assignment 1.

```bash
git clone 
pip install requirements.txt
cd assignment
```

## Usage
Just run the main.py using command bellow

### Linux 
```bash
sudo python scr/main.py
```
### Windows 
run as administrator
```bash
python scr/main.py
```

```python
from pycoingecko import CoinGeckoAPI

cg = CoinGeckoAPI()

data = cg.get_coins_markets("usd") #can be changed to other currencies


def get_market_cap(data):
    return data.get('market_cap') 


data.sort(key=get_market_cap, reverse=True)

print("Symbol: ", " ", "Current Price: ", " ", "Market capitalization: ", " ", "Market rank: ")
for i in range(len(data)):
    print(data[i]["symbol"], " ", data[i]["current_price"], " ", data[i]["market_cap"], " ", data[i]["market_cap_rank"])
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)