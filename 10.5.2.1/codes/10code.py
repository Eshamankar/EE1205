import matplotlib.pyplot as plt
import numpy as np

# Read data from the .dat file with space as the delimiter, skip lines starting with 'Values'
data = np.loadtxt('values.dat', delimiter=' ', comments='Values')

# Extracting values for x_1(n), x_2(n), x_3(n), x_4(n), and x_5(n)
n_values_1 = data[:33, 0]
x_1_values = data[:33, 1]

n_values_2 = data[34:67, 0]
x_2_values = data[34:67, 1]

n_values_3 = data[68:101, 0]
x_3_values = data[68:101, 1]

n_values_4 = data[102:135, 0]
x_4_values = data[102:135, 1]

n_values_5 = data[136:, 0]
x_5_values = data[136:, 1]

# Create the stem plots for x_1(n), x_2(n), x_3(n), x_4(n), and x_5(n)
plt.subplot(3, 2, 1)
plt.stem(n_values_1, x_1_values, linefmt='b-', markerfmt='bo', basefmt='r-')
plt.xlabel('$n$')
plt.ylabel('$x_1(n)$')
plt.grid(True)

plt.subplot(3, 2, 2)
plt.stem(n_values_2, x_2_values, linefmt='b-', markerfmt='bo', basefmt='r-')
plt.xlabel('$n$')
plt.ylabel('$x_2(n)$')
plt.grid(True)

plt.subplot(3, 2, 3)
plt.stem(n_values_3, x_3_values, linefmt='b-', markerfmt='bo', basefmt='r-')
plt.xlabel('$n$')
plt.ylabel('$x_3(n)$')
plt.grid(True)

plt.subplot(3, 2, 4)
plt.stem(n_values_4, x_4_values, linefmt='b-', markerfmt='bo', basefmt='r-')
plt.xlabel('$n$')
plt.ylabel('$x_4(n)$')
plt.grid(True)

plt.subplot(3, 2, 5)
plt.stem(n_values_5, x_5_values, linefmt='b-', markerfmt='bo', basefmt='r-')
plt.xlabel('$n$')
plt.ylabel('$x_5(n)$')
plt.grid(True)

# Adjust layout to prevent overlap
plt.tight_layout()
plt.savefig('plot.png')
# Show the combined plot
plt.show()
