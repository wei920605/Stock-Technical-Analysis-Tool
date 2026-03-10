import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# 輸入股票代號
stock_id = input("請輸入股票代號 (例如 2330.TW): ")

# 下載股票資料
data = yf.download(stock_id, period="1y")

# ===== 均線 =====
data['MA5'] = data['Close'].rolling(window=5).mean()
data['MA20'] = data['Close'].rolling(window=20).mean()

# ===== RSI 指標 =====
delta = data['Close'].diff()
gain = delta.clip(lower=0)
loss = -delta.clip(upper=0)

avg_gain = gain.rolling(14).mean()
avg_loss = loss.rolling(14).mean()

rs = avg_gain / avg_loss
data['RSI'] = 100 - (100 / (1 + rs))

# ===== MACD 指標 =====
ema12 = data['Close'].ewm(span=12).mean()
ema26 = data['Close'].ewm(span=26).mean()

data['MACD'] = ema12 - ema26
data['Signal'] = data['MACD'].ewm(span=9).mean()

# ===== 畫圖 =====
plt.figure(figsize=(12,8))

# 股價
plt.subplot(3,1,1)
plt.plot(data['Close'], label='Close')
plt.plot(data['MA5'], label='MA5')
plt.plot(data['MA20'], label='MA20')
plt.title(stock_id + " Stock Price")
plt.legend()

# RSI
plt.subplot(3,1,2)
plt.plot(data['RSI'], label='RSI')
plt.axhline(70, linestyle='--')
plt.axhline(30, linestyle='--')
plt.title("RSI Indicator")
plt.legend()

# MACD
plt.subplot(3,1,3)
plt.plot(data['MACD'], label='MACD')
plt.plot(data['Signal'], label='Signal')
plt.title("MACD Indicator")
plt.legend()

plt.tight_layout()
plt.show()
