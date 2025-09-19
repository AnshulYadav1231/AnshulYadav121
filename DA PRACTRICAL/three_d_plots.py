import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(figsize=(15,5))
theta = np.linspace(-4 * np.pi, 4 * np.pi, 100)
z = np.linspace(-2, 2, 100)
r = z**2 + 1
x = r * np.sin(theta)
y = r * np.cos(theta)

ax1 = fig.add_subplot(131, projection='3d')
ax1.plot(x, y, z); ax1.set_title("3D Line Plot")

ax2 = fig.add_subplot(132, projection='3d')
X = np.linspace(-5,5,50); Y = np.linspace(-5,5,50)
X, Y = np.meshgrid(X, Y)
Z = np.sin(np.sqrt(X**2 + Y**2))
ax2.plot_surface(X, Y, Z, cmap='viridis'); ax2.set_title("3D Surface Plot")

ax3 = fig.add_subplot(133, projection='3d')
ax3.scatter(x, y, z, c=z, cmap='plasma', s=40); ax3.set_title("3D Scatter Plot")

plt.show()
