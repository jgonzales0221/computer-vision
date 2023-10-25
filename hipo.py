# Packages
import cv2 
import numpy as np

# Open image file
img = cv2.imread ('dogs.jpeg')

# Display image in window
cv2.imshow('Original Image', img)

# Convert input image into grayscale color space
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Modify the data type
gray = np.float32(gray)

# Apply the cornerHarris method to
# detect the corner with select parameters(image, block size, ksize, and k)
dst = cv2.cornerHarris(gray, 3, 5, 0.04)

# Results are marked through dilated corners
dst = cv2.dilate(dst, None)

# Reverting back to the original image 
# with optimal threshold value
img[dst > 0.01 * dst.max()] = [0, 0, 255]

# Display image in window with cornerrs
cv2.imshow('Image with Corners', img)

# De-allocating any associated memory usage
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()
