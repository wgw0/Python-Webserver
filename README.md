# Hackathon Attempt 2

import numpy as np
import cv2 

image = cv2.imread('/Users/edisonhussey/Desktop/Saturday/image.png')

cv2.imshow('Original Image', image)
print('Image Width is',image. shape[1])
print('Image Height is',image. shape[0])
# Define Gaussian kernel
kernel_size = (15, 15)
sigma = 0
kernel = cv2.getGaussianKernel(kernel_size[0], sigma)
# kernel = np.array([[-1, -1, -1],
                            #   [-1,  9, -1],
                            #   [-1, -1, -1]])

gaussian_kernel = kernel * kernel.T

# Apply Gaussian blur
blurred_image = cv2.filter2D(image, -1, gaussian_kernel)

cv2.imshow('Blurred Image', blurred_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
