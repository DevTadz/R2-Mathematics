import numpy as np
import matplotlib.pyplot as plt

# Generate 100 points for the circle
theta = np.linspace(0, 2*np.pi, 100)
x = np.cos(theta)
y = np.sin(theta)

# Plot
plt.figure(figsize=(5,5))
plt.plot(x, y)

# Set equal aspect ratio so the circle isn't oval
plt.gca().set_aspect('equal')

plt.title("Unit Circle")
plt.grid(True)
plt.show()