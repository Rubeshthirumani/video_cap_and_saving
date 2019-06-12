import cv2
import os
cap1 = cv2.VideoCapture(0)
i=0
j=0
d=0
while(1):
	ret,frame1 = cap1.read()
	cv2.imshow('FRAME',frame1)
	#create a  new folder 
	#address of the folder where the images are to be stored 
	filename = "......./images/file_%d.jpg"%d
	#change the value of s for different frequency of storage
	s=1
	if i%s == 0:
		cv2.imwrite(filename, frame1)
	j+=1
	if cv2.waitKey(1) ==27:
		break
	d+=1
	i+=1

cap1.release()
cv2.destroyAllWindows()
