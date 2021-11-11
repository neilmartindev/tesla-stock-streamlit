import streamlit as st
import pandas as pd
import yfinance as yf
from yfinance import ticker

st.write(""""
         
## Tesla Stock Price

Below is shown the stock price and volume change of Tesla from the start of 2020 to 11/11/2021

""")

tickerSymbol = 'TSLA'

tickerData = yf.Ticker(tickerSymbol)

tickerDf = tickerData.history(period='1d', start='2020-1-01', end='2021-11-11')

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)
