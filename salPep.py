import cv2
import numpy as np
from skimage import img_as_ubyte

## original image
img = cv2.imread('dogs.jpeg', 0)
img = img/img.max() # normalize the pixel value (0~1)

# # Salt and Pepper Noise
x,y = img.shape
g = np.zeros((x,y), dtype=np.float32)
pepper = 0.1
salt = 0.95
for i in range(x):
    for j in range(y):
        rdn = np.random.random()
        if rdn < pepper:
            g[i][j] = 0
        elif rdn > salt:
            g[i][j] = 1
        else:
            g[i][j] = img[i][j]
imgNoise = g

# median filter
imgNoiseMedian = np.clip(imgNoise, -1, 1) #pixel value range
imgNoiseMedian = img_as_ubyte(imgNoiseMedian) #convert to uint8
denoiseMedian = cv2.medianBlur(imgNoiseMedian, 5)

#convert to binary
thresh, imageBlack = cv2.threshold(denoiseMedian, 130, 255, cv2.THRESH_BINARY)
#convert to median filtered grayscale 
thresh, medGray= cv2.threshold(denoiseMedian, 170.5, 255,  cv2.THRESH_TRUNC)

# preview the images
cv2.imshow('Original Image', img)
cv2.imshow('Image + Noise', imgNoise)
cv2.imshow('Denoise Median', denoiseMedian)
cv2.imshow('Binary', imageBlack) 
cv2.imshow('Median Filtered Grayscale', medGray)

# store output images
cv2.imwrite('imgNoise.png', imgNoise)
cv2.imwrite('denoiseMedian.png', denoiseMedian)
cv2.imwrite('imageBlack.png', imageBlack)
cv2.imwrite('mdeGray.png', medGray)

#break out on a key press
cv2.waitKey(0)
#clean up windows
cv2.destroyAllWindows()

    







