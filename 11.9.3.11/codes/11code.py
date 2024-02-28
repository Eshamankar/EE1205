import matplotlib.pyplot as plt
import numpy as np

def y_o(n):
    return 2 * (n + 1) + (3**(n + 2) - 1) / 2

N = 11  # Adjusted to limit the graph till n=11
n_values = np.arange(N + 1)
y_o_values = [y_o(n) for n in n_values]

plt.stem(n_values, y_o_values, basefmt='b-', linefmt='b-', markerfmt='bo')
plt.title('Stem Plot of y_o(n)')
plt.xlabel('n')
plt.ylabel('y_o(n)')

# Highlight y_o(10)
plt.annotate(f'y_o(10) = {y_o(10)}', xy=(10, y_o(10)), xytext=(8, y_o(10) + 5),
             arrowprops=dict(facecolor='red', arrowstyle='->'),
             bbox=dict(boxstyle='round,pad=0.3', edgecolor='red', facecolor='white'))

plt.show()

