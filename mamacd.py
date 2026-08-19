
# pandas DataFrame 下載台積電股票歷史股價數據 的功能


# 顯示 統計數據中的 移動平均線(股票常用 5日、10日、20日、60日、120日、240日) 以及 最高價、最低價、收盤價
#pprint(data['Close']['2330.TW'])  # 顯示收盤
# 五日均值
#data['MA5'] = data['Close']['2330.TW'].rolling(window=5).mean()
#pprint(f"5-day Moving Average: {data['Close']['2330.TW'].rolling(window=5).mean().iloc[-1]:.2%}")
# 十日均值
#data['MA10'] = data['Close']['2330.TW'].rolling(window=10).mean()
#pprint(f"10-day Moving Average: {data['Close']['2330.TW'].rolling(window=10).mean().iloc[-1]:.2%}")
# 二十日均值
#data['MA20'] = data['Close']['2330.TW'].rolling(window=20).mean()
#pprint(f"20-day Moving Average: {data['Close']['2330.TW'].rolling(window=20).mean().iloc[-1]}")

#繪製 5日、10日、20日均線圖表
#data[['Close','MA5','MA10','MA20']].plot(figsize=(12, 6))
#plt.title('TSMC 5 days MA, 10 days MA, 20 days MA')
#plt.ylabel('Price') # 設定 y軸資料名稱
#plt.show()   # 將圖表顯示出來
import ta
import yfinance as yf
from pprint import pp, pprint
import matplotlib.pyplot as plt

#ta 產出指標前需要準備 OCHLV 資料
symbol = "2330.TW"  # 台積電股票代碼
ticker = yf.Ticker(symbol)  

data = ticker.history(start="2026-03-01", end="2026-05-01", interval="1d")
#pprint(data)  # 顯示前幾筆資料

#指標定義在 SMAIndicator 類別中，使用時需要傳入收盤價資料以及計算的天數
sma_obj = ta.trend.SMAIndicator(close=data['Close'], window=5)
print(type(sma_obj))
# print(sma_obj)       列印 sma_indicator 物件的資訊(只會顯示他的 object id)

#呼叫 sma_indicator 才是真正計算五日均值的工作
data['SMA5'] = sma_obj.sma_indicator()
print(f"五日趨勢: {data['SMA5']}")

bb = ta.volatility.BollingerBands(data['Close'], window=5, window_dev=2)
data['bb_mband'] = bb.bollinger_mavg()  #中
data['bb_hband'] = bb.bollinger_hband() #上
data['bb_lband'] = bb.bollinger_lband() #下


data[['Close','bb_hband','bb_mband','bb_lband']].plot(figsize=(12, 6))
plt.title('Bollinger Band for TSMC')
plt.ylabel('value') # 設定 y軸資料名稱
plt.show()   # 將圖表顯示出來
