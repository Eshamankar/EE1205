import matplotlib.pyplot as plt

# Read data from values.dat
with open('values.dat', 'r') as file:
    values = [float(line.strip()) for line in file]

# Generate time values
time_values = [t * 0.01 for t in range(len(values))]

# Plotting stem plot
plt.stem(time_values, values, basefmt='b-', linefmt='r-', markerfmt='ro')
plt.title(r'$V_o(t) = 0.5 + \frac{0.21}{2} \sin(300t)$')
plt.xlabel('Time (s)')
plt.ylabel('V_o(t)')
plt.grid(True)
plt.show()

