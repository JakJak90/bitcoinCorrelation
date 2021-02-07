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

# Transform S&P500 data into an analysable form
spy_df = spy_df.reset_index() # In the original dataframe, the date is part of the index which means we can't select it later. 
#reset_index shifts the date into a normal column
spy_df['Date'] = spy_df['Date'].apply(lambda x: x.strftime('%Y-%m-%d')) 
spy_df['spy_returns'] = ((spy_df['Close']/spy_df['Open']) - 1) * 100
spy_returns = spy_df[['Date', 'spy_returns']]

# Pull gold price history
gold = yf.Ticker("GC=F")
gold_df = spy.history(period = 'max')

# Transform gold data into an analysable form
gold_df = gold_df.reset_index()
gold_df['Date'] = gold_df['Date'].apply(lambda x: x.strftime('%Y-%m-%d'))
gold_df['gold_returns'] = ((gold_df['Close']/gold_df['Open']) - 1) * 100 
gold_returns = gold_df[['Date', 'gold_returns']]