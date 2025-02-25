import matplotlib.pyplot as plt
import numpy as np
import random
import tkinter as tk
from tkinter import messagebox

def generate_stock_data(days):
    base_price = random.randint(100, 600)
    prices = [base_price]

    for _ in range(1, days):
        change_percent = np.random.normal(0, 1)
        new_price = prices[-1] * (1 + change_percent / 100)
        prices.append(new_price)
    return prices

days = 35
stock_prices = generate_stock_data(days)

x = np.arange(1, days + 1)
plt.figure(figsize=(10, 5))
plt.plot(x, stock_prices, linestyle='-', color='b')
plt.title('Stock Price Simulation')
plt.xlabel('Days')
plt.ylabel('Price ($)')
plt.xticks(x)
plt.grid()
plt.legend()
plt.show()