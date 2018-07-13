import numpy
import cv2

while(1):	
	#read text
	text = open('test.txt')
	img_num = text.read()
	text.close()
	if int(img_num) >5:
		#binding img
		img = cv2.imread('cap'+str(int(img_num)-4)+'.png')
		for i in range(int(img_num)-3,int(img_num)+1):
			img2 = cv2.imread('cap'+str(i)+'.png')
			img = cv2.hconcat([img,img2])
	else :
		for i in range(1,int(img_num)+1):
			if i == 1:
				img = cv2.imread('cap'+str(i)+'.png')
			else :
				img2 = cv2.imread('cap'+str(i)+'.png')
				img = cv2.hconcat([img,img2])
	#display img
	cv2.namedWindow('display',cv2.WINDOW_NORMAL)
	height = img.shape[0]
	width = img.shape[1]
	re_img = cv2.resize(img,(width*2,height*2))
	cv2.imshow('display',re_img)
	cv2.waitkey(1)