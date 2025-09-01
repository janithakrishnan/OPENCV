#! /usr/bin/env python3
import cv2
import numpy as np
import matplotlib.pyplot as plt
img=cv2.imread('coins.jpg',0)
edges=cv2.Canny(img,0,200)
edges2=cv2.Canny(img,100,200)
pic=np.hstack((img,edges,edges2))
cv2.imshow('Edge Detection using Canny',pic)
cv2.waitKey(0)
img=cv2.imread('face.jpg',0)
edges=cv2.Canny(img,0,200)
edges2=cv2.Canny(img,100,200)
pic2=np.hstack((img,edges,edges2))
cv2.imshow('Edge Detection using Canny',pic2)
cv2.waitKey(0)
