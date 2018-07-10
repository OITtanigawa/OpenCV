import numpy
import cv2

while(1):
    text = open('test.txt')
    img_num = text.read()
    text.close()

    for i in range(1,int(img_num)+1):
        if i==1:
            img = cv2.imread('cap'+str(i)+'.png')
        elif i<=5:
            img2 = cv2.imread('cap'+str(i)+'.png')
            img = cv2.hconcat([img],[img2])
        elif i >5:
            img2 = cv2.imread('cap'+str(i)+'.png')
            img = cv2.hconcat([img],[img2])
    cv2.namedWindow('test',cv2.WINDOW_NORMAL)
    cv2.imshow('test',img)
    cv2.waitkey(1)
