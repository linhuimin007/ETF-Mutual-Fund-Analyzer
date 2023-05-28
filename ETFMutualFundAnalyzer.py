import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Use numpy's random function to generate random data
np.random.seed(0)
returns = np.random.normal(0.001, 0.02, 1000)

# Generate price data, set initial price as 100
price = 100 * np.exp(returns.cumsum())

# Generate a DataFrame to store data
data = pd.DataFrame()
data['price'] = price
data['returns'] = data['price'].pct_change()

# Plot to display the data
plt.figure(figsize=(10, 5))
plt.subplot(2, 1, 1)
data['price'].plot()
plt.title('Simulated Price Data')
plt.subplot(2, 1, 2)
data['returns'].plot()
plt.title('Simulated Returns Data')
plt.tight_layout()
plt.show()
