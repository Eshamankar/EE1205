import matplotlib.pyplot as plt
import numpy as np

def x(n):
    return 2 * (n + 1) + (3**(n + 2) - 1) / 2

N = 10
n_values = np.arange(N + 1)
x_values = [x(n) for n in n_values]

plt.stem(n_values, x_values, basefmt='b-', linefmt='b-', markerfmt='bo')
plt.title('Stem Plot of x(n)')
plt.xlabel('n')
plt.ylabel('x(n)')

# Highlight x(10)
plt.annotate(f'x(10) = {x(10)}', xy=(10, x(10)), xytext=(8, x(10) + 5),
             arrowprops=dict(facecolor='red', arrowstyle='->'),
             bbox=dict(boxstyle='round,pad=0.3', edgecolor='red', facecolor='white'))

plt.show()

