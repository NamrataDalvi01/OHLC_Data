import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

ticker = "RELIANCE.NS"

data = yf.download(ticker, period="30d", interval="1d")

if isinstance(data.columns, pd.MultiIndex):
    data.columns = data.columns.get_level_values(0)

data = data[['Open', 'High', 'Low', 'Close', 'Volume']]

data.reset_index(inplace=True)

data.dropna(inplace=True)

data[['Open', 'High', 'Low', 'Close']] = data[['Open', 'High', 'Low', 'Close']].round(2)
data['Date'] = pd.to_datetime(data['Date']).dt.date


file_name = "RELIANCE_OHLC_30_Days.xlsx"
data.to_excel(file_name, index=False)

print(f"✅ Excel file saved as {file_name}")

plt.figure(figsize=(10, 5))
plt.plot(data['Date'], data['Close'])
plt.title('RELIANCE Closing Price Trend (Last 30 Days)')
plt.xlabel('Date')
plt.ylabel('Close Price')
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("RELIANCE_Trend.png")


plt.show()

print("📊 Trend chart saved as RELIANCE_Trend.png")
