#!/usr/bin/env python3
import numpy as np
import cv2 as cv
img=cv.imread('apple.jpg')
rows,cols,c=img.shape
M=np.float32([[1,0,200],[0,1,100]])
dst=cv.warpAffine(img,M,(cols*2,rows*2))
cv.imshow('Original Image',img)
cv.waitKey(0)
cv.imshow('Image after Translation',dst)
cv.waitKey(0)
