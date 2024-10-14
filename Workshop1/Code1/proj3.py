# 计算沪深300历史上的最大回撤
import pandas as pd
import numpy as np

price = pd.read_excel('000300.SH.xlsx')
close = price['收盘价'].copy()
close.dropna(inplace=True)
n = close.shape[0]
drawdown = np.zeros(n)
high = close[0]
daymax, daymin = 0, 0
for i in range(1, n):
    high = max(high, close[i])
    drawdown[i] = (high - close[i]) / high

max_drawdown = max(drawdown)
daymin = price['日期'][np.argmax(drawdown)]
daymax = price['日期'][np.argmax(close[:np.argmax(drawdown)])]
print(max_drawdown,' ',daymin,' ',daymax)

# print(price.head())