import yfinance as yf
import pprint as pprint

#print ("台積電股價資訊")
tsmc = yf.Ticker("2330.TW")
#print (f'台積電: {tsmc.history (period="30d")}')
#print (f'台積電: {tsmc.history (period="1y", interval="1mo")}')


data = yf.download("TSLA SPCX", start="2026-07-01", end="2026-08-01", interval="1wk")
pprint.pprint(data)
#pprint.pprint(tsmc.info)

#apple = yf.Ticker("AAPL")
#pprint.pprint(apple.info)

#print(tsmc.fast_info)

#print(f'台積電開盤價: {tsmc.fast_info["open"]}')
#print(f'台積電收盤價: {tsmc.fast_info["last_price"]}')
#print(f'台積電最高價: {tsmc.fast_info["day_high"]}')
#print(f'台積電最低價: {tsmc.fast_info["dayLow"]}')
#print(f'台積電上一日收盤價: {tsmc.fast_info["previous_close"]}')
#print(f'台積電上一日收盤價: {tsmc.fast_info.get("previous_close", "N/A")}')

tickers_list = "AAPL MSFT GOOG TSLA NVDA INTC AMD"
tickers = yf.Tickers(tickers_list)

#取出每一檔個股 顯示開收盤最高低價格
#for ticker in tickers.tickers.values():
#    print(f"{ticker.ticker} 基本資訊")    
#    print(f"{ticker.ticker} 目前價格: {ticker.fast_info['lastPrice']}")
 #   print(f"{ticker.ticker} 昨日收盤價格: {ticker.fast_info['previousClose']}")
  #  print(f"{ticker.ticker} 今日開盤價格: {ticker.fast_info['open']}")    
   # print(f"{ticker.ticker} 今日最高價格: {ticker.fast_info['dayHigh']}")
    #print(f"{ticker.ticker} 今日最低價格: {ticker.fast_info.get('dayLow', '無')}")
    #print("=====================================")

