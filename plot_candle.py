# import plotly.graph.objects as go 
import pandas as pd
import talib
import numpy as np
import yfinance as yf 
import os, pandas
import datetime
import time
import mplfinance as mpf
import matplotlib.pyplot as plt

start = "2020-06-01"
end = datetime.datetime.now()
# end = "2021-07-09"
# end = "2021-06-30"
tickers = ["AMANAH","ASAP"]  #['STHAI', 'MAX', 'PE', 'PACE', 'POLAR', 'GSTEEL', 'STOWER', 'TWZ', 'KC', 'EMC', 'GEL', 'BSM', 'GL', 'STAR', 'NOK', 'TVD', 'SITHAI', 'MONO', 'A5', 'TPIPL', 'TPOLY', 'L&E', 'CPL', 'TITLE', 'AIRA', 'PDJ', 'WINNER', 'NNCL', 'CEN', 'TSE', 'LOXLEY', 'KUN', 'PPM', 'TRT', 'KK', 'TNPC', 'MK', 'SHR', 'SC', 'ACE', 'CHOW', 'CHG', 'LHK', 'PHOL', 'IHL', 'NINE', 'THANI', 'WHAUP', 'TFG', 'AWC', 'DEMCO']
for ticker in tickers:
    data = yf.download(ticker +".BK", start, end)
    candle = mpf.plot(data, type='candle', volume=True, mav=(5,15,35), title=ticker)

    # plt.savefig(f'./daily_stock/{ticker}' + '.png')
print(candle)



