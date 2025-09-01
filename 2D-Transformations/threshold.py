#! /usr/bin/env python3
import cv2
import numpy as np
import matplotlib.pyplot as plt
img=cv2.imread('gradient.jpg',0)
ret,thresh1=cv2.threshold(img,127,255,cv2.THRESH_BINARY)
ret,thresh2=cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
ret,thresh3=cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
ret,thresh4=cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
ret,thresh5=cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)
titles=['Gray scaled Image','Threshold-Binary','Threshold_BINARY_INV', 'Threshold TRUNC', 'TOZERO','TOZERO_INV']
images=[img,thresh1,thresh2,thresh3,thresh4,thresh5]
for i,image in enumerate(images):
	plt.subplot(2,3,i+1)
	plt.imshow(image,cmap='gray')
	plt.title(titles[i])
	plt.xticks([])
	plt.yticks([])
plt.show() 
