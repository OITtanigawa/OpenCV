import numpy
import cv2

text = open('test.txt')
img_num = text.read()
text.close()
img = cv2.imread(img_num+".png")
cv2.namedWindow('test',cv2.WINDOW_NORMAL)
#img_g = cv2.imread(img_num+".png")
cv2.imshow('test',img)
#cv2.imshow("gray",img_g)
cv2.waitkey(0)
