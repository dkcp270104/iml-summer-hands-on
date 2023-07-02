import numpy as np
import matplotlib.pyplot as plt

# Set the values
N = 50
S_values = np.arange(1, N + 1)
theta_values = np.linspace(0.1, 0.9, 100)

# Likelihood Estimate
S_grid, theta_grid = np.meshgrid(S_values, theta_values)
likelihood = S_grid * np.log(theta_grid) + (N - S_grid) * np.log(1 - theta_grid)

# Install qt (comment: not sure why it's mentioned here, as it's not used in the code)

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
surface = ax.plot_surface(S_grid, theta_grid, likelihood, cmap='jet')
ax.set_xlabel('S')
ax.set_ylabel('theta')
ax.set_zlabel('L(theta|S)')
ax.view_init(65, 15)

# Save the plot as an image
plt.savefig("sThetaL-py.png")

# Display the plot (comment: the original code had plt.show() commented out)
# plt.show()
