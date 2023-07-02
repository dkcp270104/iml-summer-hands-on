import cv2
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

# Read the image
image_path = './shadow.tif'
image = cv2.imread(image_path)

# Convert the image to grayscale and normalize the values
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) / 255

# Set the number of iterations
T = 100

# Repeat the grayscale image along the third axis to match the number of iterations
repeated_image = np.repeat(gray_image[:, :, np.newaxis], T, axis=2)

# Generate Poisson random variables
poisson_variables = stats.poisson.rvs(repeated_image)

# Threshold the variables
thresholded_variables = (poisson_variables >= 1).astype(float)

# Estimate the parameter lambda_hat
lambda_hat = -np.log(1 - np.mean(thresholded_variables, axis=2))

# Display the estimated lambda_hat
plt.imshow(lambda_hat, cmap='gray')
#plt.show()
plt.savefig('5b-tif.png')