# This project was done to gain a basic understanding of how Pandas works for data gathering
# and analysis

import pandas as pd # Data analysis package
import json # Package required to use JSON data files
from urllib.request import urlopen # Package enabling opening of websites and using APIs
import yfinance as yf # Yahoo Finance 
from datetime import datetime 

# Pull bitcoin proce history
btc_url = "https://min-api.cryptocompare.com/data/v2/histoday?fsym=BTC&tsym=USD&limit=2000&api_key=d1875a3943f6f2ee83a90ac2e05d5fa018618e00724e9018f9bd08c0ac932cc6"
btc_data = urlopen(btc_url).read() # Open the API contents 
btc_json = json.loads(btc_data) # Output response in JSON format

