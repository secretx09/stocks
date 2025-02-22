import matplotlib.pyplot as plt
import numpy as np

x = [1, 2, 3, 4, 5]
y = [100, 200, 300, 400, 500]

plt.plot(x, y, linestyle='-', color='blue')
plt.fill_between(x, 0, y, alpha=.3)
plt.title('My Line Graph')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

plt.show()