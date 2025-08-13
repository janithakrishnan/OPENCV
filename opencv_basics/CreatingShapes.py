import numpy as np
import cv2 as cv
img=np.zeros([512,512,3])
cv.line(img,(10,10),(500,10),(0,0,255),3)
cv.line(img,(20,20),(500,20),(0,255,0),3)
cv.rectangle(img,(30,30),(100,100),(0,255,255),2)
cv.circle(img,(300,300),30,(255,255,0),1)
cv.ellipse(img,(150,300),(100,75),0,0,360,(0,255,255),-1)
font=cv.FONT_HERSHEY_SIMPLEX
cv.putText(img,'OpenCV',(10,400),font,2,(255,0,255),3) #font size =2 , thickness=3
cv.imshow('question2',img)
cv.waitKey(0)
