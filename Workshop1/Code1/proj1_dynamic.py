import pandas as pd
import datetime as dt
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation

# 读取并处理数据
minute_data = pd.read_csv('000300.SH_1min.csv', index_col=0)
minute_data.index = pd.to_datetime(minute_data.index)

# 只关注2023-12-01的数据
last_dt = dt.datetime(2023, 12, 2, 9) 
minute_data = minute_data[minute_data.index <= last_dt]

# 窗口大小
window_size = 30

# 设置图形
fig, ax = plt.subplots()

def update(frame):
    # 获取当前滑动窗口的数据
    window_data = minute_data.iloc[frame:frame + window_size]

    # 清空之前的图形
    ax.clear()

    # 绘制滑动窗口内的K线
    for i in range(window_data.shape[0]):
        o = window_data['open'][i]
        c = window_data['close'][i]
        color = 'r' if c > o else 'g'
        ax.plot([i, i], [window_data['low'][i], window_data['high'][i]], color)
        ax.bar(i, abs(c - o), 0.5, min(c, o), color=color)
    
    # 设置X轴的刻度
    ax.set_xticks(range(0, window_size, 5))
    ax.set_xticklabels(window_data.index.strftime('%H:%M')[::5], rotation=45)

    # 动态设置Y轴范围
    ax.set_ylim(window_data['low'].min(), window_data['high'].max())
    
    # 添加标题和标签
    ax.set_title('000300.SH on 2023-12-01 (Sliding Window)')
    ax.set_xlabel('Time')
    ax.set_ylabel('Price')

# 创建动画，间隔200毫秒，逐帧更新
ani = FuncAnimation(fig, update, frames=range(len(minute_data) - window_size), interval=200)

plt.show()
