# This project was done to gain a basic understanding of how Pandas works for data gathering
# and analysis and was completed as part of a tutorial

import pandas as pd # Data analysis package
import json # Package required to use JSON data files
from urllib.request import urlopen # Package enabling opening of websites and using APIs
import yfinance as yf # Yahoo Finance 
from datetime import datetime 

# Pull bitcoin proce history
btc_url = "https://min-api.cryptocompare.com/data/v2/histoday?fsym=BTC&tsym=USD&limit=2000&api_key=adc77c4c1378ed8f7f43fef0b282d6773a735f98fed387e2311b5534aaa5bdfb"
btc_data = urlopen(btc_url).read() # Open the API contents 
btc_json = json.loads(btc_data) # Output response in JSON format

# Transform Bitcoin data into an analysable form
btc_price = btc_json['Data']['Data'] # Extract relevant data from the JSON variable
btc_df = pd.DataFrame(btc_price) # Convert the json format into a Pandas dataframe, making it easier to work with 
btc_df['btc_returns'] = ((btc_df['close']/btc_df['open']) - 1) * 100 # Create a coloumn for daily returns of Bitcoin 
btc_df['Date'] = btc_df['time'].apply(lambda x: datetime.utcfromtimestamp(x).strftime('%Y-%m-%d')) # Formatting the date into a human-readable format
btc_returns = btc_df[['Date', 'btc_returns']] # Select the only 2 columns we'll need for our correlation calculations, namely the Date and the Return


# Pull S&P500 price history
spy = yf.Ticker("SPY")
spy_df = spy.history(period = 'max')

# Pull gold price history
spy = yf.Ticker("GC=F")
spy_df = spy.history(period = 'max')

