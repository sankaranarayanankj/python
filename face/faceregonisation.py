import cv2
import os
import numpy as np


def faceDetection(test_img):
	gray_img=cv2.cvtColor(test_img,cv2.COLOR_BGRGRAY)
	face_haar_cascade=cv2.CascadeClassifier('/haarcascade_frontalface_default.xml')
	faces=face_haar_cascade.detectMultiScale(gray_img,scaleFactor=1.32,minNeighbours=5)

	return faces,gray_img