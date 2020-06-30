import cv2 as cv
import numpy as np
img = cv.imread('BW.jpg')
cv.imshow('image',img)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
gray = np.float32(gray)
dat = cv.cornerHarris(gray,2,3,0.04)
dst = cv.dilate(dat,None)
img[dst>0.01* dst.max()]=[0,0,255]
cv.imshow('Result',img)
if cv.waitKey(0) & 0xff == 27:
    cv.destroyWindow()
