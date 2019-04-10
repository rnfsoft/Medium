# https://towardsdatascience.com/implementing-macd-in-python-cc9b2280126a

import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt
import pyEX as p
from pandas.plotting import register_matplotlib_converters

register_matplotlib_converters()

ticker = 'GRPN'
timeframe = '6m'

df = p.chartDF(ticker, timeframe)
df = df[['close']]
df.reset_index(level=0, inplace=True)
df.columns=['ds','y']

# plt.plot(df.ds, df.y, label=ticker)
# plt.show()

# MACD vs the signal line
exp1 = df.y.ewm(span=12, adjust=False).mean()
exp2 = df.y.ewm(span=26, adjust=False).mean()

macd = exp1 - exp2
exp3 = macd.ewm(span=9, adjust=False).mean()

# plt.plot(df.ds, macd, label=ticker + ' MACD', color = '#EBD2BE')
# plt.plot(df.ds, exp3, label='Signal Line', color='#E5A4CB')
# plt.legend(loc='upper left')
# plt.show() # bullish crossover: MACD crosses above signal line

# EMA(Exponentail Moving Averages) and MACD
exp1 = df.y.ewm(span=12, adjust=False).mean()
exp2 = df.y.ewm(span=26, adjust=False).mean()
exp3 = df.y.ewm(span=9, adjust=False).mean()

macd = exp1-exp2

plt.plot(df.ds, df.y, label=ticker)
plt.plot(df.ds, macd, label=ticker + ' MACD', color='orange')
plt.plot(df.ds, exp3, label='Signal Line', color='Magenta')
plt.legend(loc='upper left')
plt.show()


