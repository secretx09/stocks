#pip install matplotlib pandas yfinance

import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
import pandas as pd
import yfinance as yf

class StockChartApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Stock Chart App")

        # Create a frame for the input
        self.frame = ttk.Frame(self.root)
        self.frame.pack(pady=20)

        # Entry for stock ticker
        self.ticker_label = ttk.Label(self.frame, text="Enter Stock Ticker:")
        self.ticker_label.grid(row=0, column=0)

        self.ticker_entry = ttk.Entry(self.frame)
        self.ticker_entry.grid(row=0, column=1)

        # Button to fetch and plot data
        self.plot_button = ttk.Button(self.frame, text="Plot Stock Chart", command=self.plot_stock_chart)
        self.plot_button.grid(row=0, column=2)

    def plot_stock_chart(self):
        ticker = self.ticker_entry.get()
        if ticker:
            # Fetch stock data
            stock_data = yf.download(ticker, start="2022-01-01", end="2023-01-01")
            if not stock_data.empty:
                # Plotting the stock data
                plt.figure(figsize=(10, 5))
                plt.plot(stock_data['Close'], label='Close Price')
                plt.title(f'Stock Price for {ticker}')
                plt.xlabel('Date')
                plt.ylabel('Price (USD)')
                plt.legend()
                plt.grid()
                plt.show()
            else:
                print("No data found for the ticker.")
        else:
            print("Please enter a valid ticker.")

if __name__ == "__main__":
    root = tk.Tk()
    app = StockChartApp(root)
    root.mainloop()
