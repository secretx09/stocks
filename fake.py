import numpy as np
import matplotlib.pyplot as plt

# Function to generate random stock-like data
def generate_stock_data(days):
    # Start with a base price
    base_price = 100
    prices = [base_price]

    # Generate random price changes
    for _ in range(1, days):
        # Randomly change the price by a small percentage
        change_percent = np.random.normal(0, 1)  # Mean 0, Std Dev 1
        new_price = prices[-1] * (1 + change_percent / 100)
        prices.append(new_price)

    return prices

# Number of days for the chart
days = 30
stock_prices = generate_stock_data(days)

# Create a time series for the x-axis
x = np.arange(1, days + 1)

# Plotting the stock-like data
plt.figure(figsize=(10, 5))
plt.plot(x, stock_prices, linestyle='-', color='b', label='Simulated Price')
plt.title('Simulated Stock-like Price Over Time')
plt.xlabel('Days')
plt.ylabel('Price ($)')
plt.xticks(x)  # Set x-ticks to be the days
plt.grid()
plt.legend()
plt.show()