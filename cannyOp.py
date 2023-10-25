# Packages
import cv2
import numpy as np

#open image file
img = cv2.imread('dogs.jpeg')

# Convert image to canny image and store output image
cv2.imwrite('canny.jpeg', cv2.Canny(img, 50, 100)) # image, threshold 1 (100) & 2 (300) 

# Autocanny
sigma = 0.3
median = np.median(img)

# apply automatic Canny edge detection using the computed median
lower = int(max(0,(1.0 - sigma) * median))
# Lower thrershold is sigma % lower than median
# If value is below 0 then take 0 as the value

upper = int(min(255,(1.0 + sigma) * median))
# Upper threshold is sigma % higher than median
# If the value is larger than 255 then take 255 as the value

autoCanny = cv2.Canny(img, lower, upper)
# (Bhattiprolu, 2020). 

# Display image in window
cv2.imshow('Canny Dogs', cv2.imread('canny.jpeg'))
cv2.imshow('Original Dogs', cv2.imread('dogs.jpeg'))
cv2.imshow ('Auto Canny', autoCanny)

# Break out on a key presss
cv2.waitKey(0)

# Clean up Windows
cv2.destroyAllWindows()