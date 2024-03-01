import matplotlib.pyplot as plt
import numpy as np

# Read data from the .dat file with space as the delimiter, skip lines starting with 'Values'
data = np.loadtxt('values_v.dat', delimiter=' ', comments='Values')

# Extracting values for V_o(t)
t_values = data[:, 0]
V_o_values = data[:, 1]

# Create the stem plot for V_o(t)
plt.stem(t_values, V_o_values, linefmt='b-', markerfmt='bo', basefmt='r-')
plt.xlabel('$t$')
plt.ylabel('$V_o(t)$')
plt.grid(True)

plt.savefig('Vo_plot.png')
# Show the plot
plt.show()

