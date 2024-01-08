import matplotlib.pyplot as plt
import numpy as np

# Define the function for the summation
def summation_function(k):
    return np.sum(2 + 3**np.arange(1, k+1))

# Generate values for k from 1 to 11
k_values = np.arange(1, 12)

# Calculate the corresponding summation values
summation_values = [summation_function(k) for k in k_values]

# Plot the graph
plt.plot(k_values, summation_values, marker='o', linestyle='-')
plt.title('Graph of Summation $2 + 3^k$ from $k=1$ to $k=11$')
plt.xlabel('k')
plt.ylabel('Summation Value')
plt.grid(True)
plt.show()
