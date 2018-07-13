import numpy
import cv2

flag = 0
while(1):	
	#read text
	text = open('test.txt')
	img_num = text.read()
	text.close()
	if int(img_num) >5:
		#binding img
		for i in range(int(img_num)-5,int(img_num)):
			if i%5 == 1:
				img = cv2.imread('cap'+str(i)+'.png')
			else :
				img2 = imread('cap'+str(i)+'.png')
				img = cv2.hconcat([img,img2])
	else :
		for i in range(int(img_num)-5,int(img_num)):
			if i == 1:
				img = cv2.imread('cap'+str(i)+'.png')
			else :
				img2 = imread('cap'+str(i)+'.png')
				img = cv2.hconcat([img,img2])
	#display img
	cv2.namedWindow('display',cv2.WINDOW_NORMAL)
	cv2.imshow('display',img)
	cv2.waitkey(1)