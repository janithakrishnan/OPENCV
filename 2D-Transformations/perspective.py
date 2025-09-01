#! /usr/bin/env python3
import cv2
import numpy as np
import matplotlib.pyplot as plt
img=cv2.imread('sudoku.png')
rows,cols,c=img.shape
pts1=np.float32([[56,50],[300,200],[28,98],[380,370]])
pts2=np.float32([[0,0],[500,0],[0,500],[500,500]])
M=cv2.getPerspectiveTransform(pts1,pts2)
dst=cv2.warpPerspective(img,M,(500,500))
plt.subplot(121)
plt.imshow(img)
plt.title('Input Image')
plt.subplot(122)
plt.imshow(dst)
plt.title('Output Image')
plt.show()
