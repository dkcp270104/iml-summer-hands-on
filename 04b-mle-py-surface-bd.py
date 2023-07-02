import numpy as np
import matplotlib.pyplot as plt

N = 50
S_values = np.arange(1, N, 0.1)
theta_values = np.linspace(0.1, 0.9, 100)

# Create a figure with two subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))
fig.suptitle("Maximum Likelihood Estimation")

# Plot the likelihood as a heatmap
heatmap = ax1.imshow(
    S_values[:, np.newaxis] * np.log(theta_values) + (N - S_values[:, np.newaxis]) * np.log(1.0 - theta_values),
    cmap='jet',
    origin='lower',
    aspect='auto',
    extent=[S_values.min(), S_values.max(), theta_values.min(), theta_values.max()]
)
ax1.set_xlabel('S')
ax1.set_ylabel('θ')
ax1.set_title("Bird's Eye View")

# Add a vertical line at S = 25
ax1.axvline(x=25, color='black')

# Plot L(θ|S=25)
ax2.plot(theta_values, 25 * np.log(theta_values) + (N - 25) * np.log(1.0 - theta_values), color='blue')
ax2.set_xlabel('θ')
ax2.set_title("L(θ|S=25)")

# Adjust spacing between subplots
plt.subplots_adjust(wspace=0.5)

# Save the figure
plt.savefig("sThetaL25-py-bd.png")
