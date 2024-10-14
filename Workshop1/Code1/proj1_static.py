# 这段代码可以直播演示
import pandas as pd
import datetime as dt
from matplotlib import pyplot as plt

minute_data = pd.read_csv('000300.SH_1min.csv',index_col=0)
minute_data.index = pd.to_datetime(minute_data.index)

# Temporarily we only focus on the data of 2023-12-01
last_dt = dt.datetime(2023,12,2,9) 
minute_data = minute_data[minute_data.index <= last_dt]

fig, ax = plt.subplots()
n = minute_data.shape[0]
for i in range(n):
    o = minute_data['open'][i]
    c = minute_data['close'][i]
    color = 'r' if c > o else 'g'
    ax.plot([i, i],[minute_data['low'][i], minute_data['high'][i]], color)
    ax.bar(i, abs(c - o), 0.5, min(c, o), color=color)

ax.set_xticks(range(0, n, 30))
ax.set_xticklabels(minute_data.index.strftime('%H:%M')[::30], rotation=45)
ax.set_title('000300.SH on 2023-12-01')
ax.set_xlabel('Time')
ax.set_ylabel('Price')

plt.show()