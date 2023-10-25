# Packages
import cv2 

# Load innput image
img = cv2.imread('lenna.jpeg')

# Using Gaussin filter
gausBlur = cv2.GaussianBlur(img, (1,1), 0) #sigma 1
gausBlur2 = cv2.GaussianBlur(img, (5,5), 0) #sigma5
gausBlur3 = cv2.GaussianBlur(img, (11,11), 0) #sigma 11

# Preview images
cv2.imshow ('Original Lenna', img)
cv2.imshow('Gaussian Lenna 1', gausBlur)
cv2.imshow('Gaussian Lenna 5', gausBlur2)
cv2.imshow('Gaussian Lenna 11', gausBlur3)

# Break out on a key presss
cv2.waitKey(0)

# Clean up Windows
cv2.destroyAllWindows()