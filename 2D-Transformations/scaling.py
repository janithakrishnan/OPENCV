#! /usr/bin/env python3
import cv2 as cv
import numpy as np
img=cv.imread('apple.jpg')
res=cv.resize(img,None,fx=2,fy=2)#scaling factor 2 on both x and y axes
cv.imshow('Original Image',img)
cv.waitKey(0)
cv.imshow('Image after Scaling',res)
cv.waitKey(0)
img_gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
res_gray=cv.resize(img_gray,None,fx=2,fy=2)#scaling factor 2 on both x and y axes
cv.imshow('Original Image in gray scale',img_gray)
cv.waitKey(0)
cv.imshow('Image after Scaling',res_gray)
cv.waitKey(0)

