import yfinance as yf
from pprint import pp, pprint
import matplotlib.pyplot as plt


# pandas DataFrame 下載台積電股票歷史股價數據 的功能

data = yf.download(["2330.TW"], start="2026-03-01", end="2026-05-01", interval="1d")
# 顯示 統計數據中的 移動平均線(股票常用 5日、10日、20日、60日、120日、240日) 以及 最高價、最低價、收盤價
#pprint(data['Close']['2330.TW'])  # 顯示收盤
# 五日均值
data['MA5'] = data['Close']['2330.TW'].rolling(window=5).mean()
#pprint(f"5-day Moving Average: {data['Close']['2330.TW'].rolling(window=5).mean().iloc[-1]:.2%}")
# 十日均值
data['MA10'] = data['Close']['2330.TW'].rolling(window=10).mean()
#pprint(f"10-day Moving Average: {data['Close']['2330.TW'].rolling(window=10).mean().iloc[-1]:.2%}")
# 二十日均值
data['MA20'] = data['Close']['2330.TW'].rolling(window=20).mean()
#pprint(f"20-day Moving Average: {data['Close']['2330.TW'].rolling(window=20).mean().iloc[-1]}")

#繪製 5日、10日、20日均線圖表
data[['Close','MA5','MA10','MA20']].plot(figsize=(12, 6))
plt.title('TSMC 5 days MA, 10 days MA, 20 days MA')
plt.ylabel('Price') # 設定 y軸資料名稱
plt.show()   # 將圖表顯示出來
