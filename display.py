import numpy
import cv2

flag = 0
while(1):
	#init img
	img = None
	
	#read text
	text = open('test.txt')
	img_num = text.read()
	text.close()

	#binding img
	for i in range(int(img_num)-5,int(img_num)):
		if i%5 == 1:
			img = cv2.imread('cap'+str(i)+'.png')
		else :
			img = cv2.hconcat([img],[cv2.imread('cap'+str(i)+'.png')])
	
	#display img
	cv2.namedWindow('display',cv2.WINDOW_NORMAL)
	cv2.imshow('display',img)
	cv2.waitkey(1)