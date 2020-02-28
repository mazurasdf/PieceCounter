from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
import json

import cv2
import cv2 as cv
import numpy as np
import imutils
from imutils import contours
from scipy.spatial import distance as dist
import os
import base64
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

os.chdir("./puzzle_pieces/temp_image")
# Create your views here.
def buttonClick(request):
	print("clicked on the backend too!")
	data = {
		"stuff": 0
	}
	return JsonResponse(data)

def receivePic(request):
	img = request.FILES['image']
	path = default_storage.save('temp_img.jpg', ContentFile(img.read()))
	img = cv2.imread(path)
	gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
	ret, thresh = cv.threshold(gray,0,255,cv.THRESH_BINARY_INV+cv.THRESH_OTSU)
	image = (thresh)

	edged=cv2.Canny(image,40,350)
	edged = cv2.GaussianBlur(edged, (5, 5), 0)
	contours=cv2.findContours(edged,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
	
	contours = imutils.grab_contours(contours)
	count = 0
	sum = 0
	avg = 0
	# for c in range(len(contours)):
	#   sum += cv2.contourArea(contours[c])
	# avg = sum/len(contours)
	
	output = []
	for cnt in range(len(contours)):
		if cv2.contourArea(contours[cnt]) > 400:
			# cv2.drawContours(image,contours[cnt],-1,(0,200,0),10)
			count +=1
			output.append(contours[cnt])
	similarity = cv2.matchShapes(output[0], output[4], 1, 0)
	print(similarity)
	# cv2.imshow('contours',image)
	# cv2.waitKey(0)

	# adds the green outlines to the original image
	cv2.drawContours(img,output,-1,(0,0,255),10)
	cv2.imwrite("outlines.jpg", img)
	cv2.imwrite("threshold.jpg", image)
	# cv2.imshow("window", cv2.resize(img,(int(img.shape[1]/3),int(img.shape[0]/3))))
	# cv2.waitKey(0)

	with open("outlines.jpg", "rb") as image_file:
		x = base64.b64encode(image_file.read())
	with open("threshold.jpg", "rb") as threshold_file:
		y = base64.b64encode(threshold_file.read())
	encoded_string = json.dumps(x.decode("utf-8"))
	threshold_string = json.dumps(y.decode("utf-8"))

	encoded_string = encoded_string[:-1]
	encoded_string = encoded_string[1:]
	threshold_string = threshold_string[:-1]
	threshold_string = threshold_string[1:]

	data = {
		"count": count,
		"imgData": encoded_string,
		"threshData": threshold_string
	}
	return JsonResponse(data)