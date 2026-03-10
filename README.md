# Stock-Technical-Analysis-Tool
# 股票技術指標分析工具 (Stock Technical Analysis Tool)

這是一個基於 Python 開發的輕量化金融數據分析腳本。透過抓取 Yahoo Finance 的即時市場數據，自動計算並繪製多種技術分析指標圖表，輔助投資決策。

## 📈 功能亮點
* **自動化數據串接**：使用 `yfinance` 獲取全球股市（如台股、美股）的歷史成交資料。
* **技術指標運算**：
    * **均線 (Moving Average)**：計算 5 日與 20 日均線，觀察短期與中期趨勢。
    * **RSI (相對強弱指標)**：分析市場買氣，判斷是否過熱（超買）或過冷（超賣）。
    * **MACD (平滑異同移動平均線)**：判斷股價動能與多空交叉訊號。
* **數據視覺化**：整合 `matplotlib` 繪製三合一圖表，方便一目了然股價與指標的連動。

## 🛠️ 技術棧
* **語言**: Python 3.x
* **數據處理**: Pandas
* **數據來源**: yfinance API
* **圖表繪製**: Matplotlib

## 🚀 快速上手
1. **安裝環境**:
   ```bash
   pip install yfinance pandas matplotlib
   執行程式:
直接執行腳本，並依照提示輸入股票代號（例如：2330.TW 或 AAPL）。

產出結果:
程式將自動生成包含股價、RSI、MACD 三個區塊的互動式分析圖表。

透過這個專案，我實作了如何處理時間序列數據 (Time-series data)，並練習將複雜的金融公式轉化為程式邏輯。這展現了我在數據處理、API 對接以及資訊視覺化方面的基礎能力。
