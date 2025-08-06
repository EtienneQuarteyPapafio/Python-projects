import numpy as np #imports the numpy library and gives it a custom function name
import matplotlib.pyplot as plt #imports the matplot library and gives it a custom function name

# Generate x values from 0 to 2π (one full cycle)
x = np.linspace(0, 2 * np.pi, 1000)

# Calculate y values (sine of x)
y = np.sin(x)

# Plot the sine wave
plt.plot(x, y)

# Add title and labels
plt.title("Sine Wave")
plt.xlabel("x (radians)")
plt.ylabel("sin(x)")

# Show grid and the plot
plt.grid(True)
plt.show()
