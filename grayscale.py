#packages
import cv2

# open image file
image = cv2.imread('dogs.jpeg', cv2.IMREAD_UNCHANGED)

#convert image to grayscale
image_grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

image_median = cv2.medianBlur(image, 5)

# convert image to black and white
thresh, image_black = cv2.threshold(image_grayscale, 120, 255, cv2.THRESH_BINARY)

#display image in window
cv2.imshow('dogs.jpeg', image)  #default view

#convert image to grayscale
cv2.imshow('dogs.jpeg', image_grayscale)  #grayscale view

#convert image to black and white
cv2.imshow('dogs.jpeg', image_black)   #black and white view

#store output images
cv2.imwrite('image_grayscale.png', image_grayscale)
cv2.imwrite('image_black.png', image_black)

#break out on a key press
cv2.waitKey(0)

#clean up windows
cv2.destroyAllWindows()