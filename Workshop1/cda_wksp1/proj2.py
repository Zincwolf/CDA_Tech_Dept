import pandas as pd
import datetime as dt
from math import ceil
import numpy as np
from typing import Union

def rank(r: Union[float, np.float64]) -> np.float64:
    '''
    分级靠档
    '''
    if r<=0.15:
        return round(r, 2)
    if r>=0.8:
        return 1
    return ceil(r*10)/10

def process(df: pd.DataFrame) -> pd.DataFrame:
    df['free_ratio'] = df['自由流通股本(亿)'] / df['总股本(亿)']
    df['w_ratio'] = df['free_ratio'].apply(rank)
    df['adj_stk_cap'] = df['总股本(亿)'] * df['w_ratio']
    df['adj_mkt_cap'] = df['adj_stk_cap'] * df['收盘价(原始币种)']
    return df

# l = np.random.rand(10)
# print(l)
# print(list(map(rank, l)))

d0927 = pd.read_excel('000300_weight_20240927.xlsx', index_col=0)
d0930 = pd.read_excel('000300_weight_20241003.xlsx', index_col=0)
d0927 = process(d0927)
d0930 = process(d0930)
idx0927 = d0927['adj_mkt_cap'].sum()
idx0930 = d0930['adj_mkt_cap'].sum()

# print(d0927.head())
# print(idx0927)
# print(d0930.head())
# print(idx0930)

print(idx0927/idx0930)