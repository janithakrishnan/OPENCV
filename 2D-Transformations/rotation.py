#! /usr/bin/env python3
import numpy as np
import cv2 as cv
img=cv.imread('apple.jpg')
rows,cols,c=img.shape
M=cv.getRotationMatrix2D(((cols-1)/2.0,(rows-1)/2.0),45,1)
dst=cv.warpAffine(img,M,(cols,rows))
cv.imshow('Original Image',img)
cv.waitKey(0)
cv.imshow('Rotated Image',dst)
cv.waitKey(0)
