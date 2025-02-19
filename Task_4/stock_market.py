# Step1: Extract stock price data using Yahoo Finance API.
import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

def get_stock_data(ticker, start, end):
    stock = yf.download(ticker, start=start, end=end, period= "1y")
    return stock

data = get_stock_data("AAPL", "2023-01-01", "2024-01-01")
#print(data.head())
print(data)

#----------------------------------------------------------------------

# Step2: Perform time series analysis on stock prices.
# Plot stock price trends
def plot_stock_price(data):
    plt.figure(figsize=(12, 6))
    plt.plot(data.index, data['Close'], label="Closing Price", color='blue')
    plt.title("Stock Price Over Time")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.legend()
    plt.show()

plot_stock_price(data)

#----------------------------------------------------------------------

# Step3: Use moving averages and RSI indicators to identify buying/selling opportunities.
# Compute Moving Averages
data['SMA_50'] = data['Close'].rolling(window=50, min_periods=1).mean()
data['SMA_200'] = data['Close'].rolling(window=200, min_periods=1).mean()

def compute_rsi(data, window=14):
    delta = data['Close'].diff()  # Compute daily price change

    gain = np.where(delta > 0, delta, 0).flatten()  # Ensure 1D array
    loss = np.where(delta < 0, -delta, 0).flatten()  # Ensure 1D array

    avg_gain = pd.Series(gain, index=data.index).rolling(window=window, min_periods=1).mean()
    avg_loss = pd.Series(loss, index=data.index).rolling(window=window, min_periods=1).mean()

    rs = avg_gain / avg_loss
    data['RSI'] = 100 - (100 / (1 + rs))

    return data

# Apply the function
data = compute_rsi(data)

# Print the last few rows
print(data[['Close', 'SMA_50', 'SMA_200', 'RSI']].tail(15))

#---------------------------------------------------------------------------

#Step4: Create a dashboard using Streamlit or Dash.

st.title("Stock Price Analysis")

ticker = st.text_input("Enter Stock Ticker", "AAPL")
start_date = st.date_input("Start Date", pd.to_datetime("2023-01-01"))
end_date = st.date_input("End Date", pd.to_datetime("2024-01-01"))

if st.button("Get Data"):
    data = get_stock_data(ticker, start_date, end_date)
    st.line_chart(data[['Close', 'SMA_50', 'SMA_200']])
    st.write(data.tail())

st.write("RSI Analysis")
st.line_chart(data['RSI'])

#-----------------------------------------------------------------------------------------------








