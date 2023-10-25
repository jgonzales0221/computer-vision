import cv2
import numpy as np
from skimage import img_as_ubyte

imgBlk = cv2.imread('imageBlack.png', 0)
imgBlk = imgBlk/imgBlk.max()

#Gaussian Noise
# x, y = imgBlk.shape
# mean = 0
# var = 0.1
# sigma = np.sqrt(var)
# n = np.random.normal(loc=mean, 
#                      scale=sigma, 
#                      size=(x,y))
# imgNoise = imgBlk + n

#salt and pepper noise
x,y = imgBlk.shape
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
            g[i][j] = imgBlk[i][j]

imgNoise = g


#median filter
imgNoiseMed = np.clip(imgNoise, -1, 1)

#range 
imgNoiseMed = img_as_ubyte(imgNoiseMed, 5)

denoiseMed = cv2.medianBlur(imgNoiseMed, 5)
rgbImg = cv2.cvtColor(denoiseMed, cv2.COLOR_GRAY2RGB)

cv2.imshow('Black and White', imgBlk)
cv2.imshow('Image + Noise', imgNoise)
cv2.imshow('Median Filtered', denoiseMed)
cv2.imshow('Filtered grayscale', rgbImg)



#break out on a key press
cv2.waitKey(0)

#clean up windows
cv2.destroyAllWindows()