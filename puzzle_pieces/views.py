from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse

import cv2
import cv2 as cv
import numpy as np
import imutils
from imutils import contours
from scipy.spatial import distance as dist
import os
import base64

# Create your views here.
def buttonClick(request):
	print("clicked on the backend too!")
	data = {
		"stuff": 0
	}
	return JsonResponse(data)

def receivePic(request):
	print(request.FILES['image'].name)

	img = request.FILES['image']
	img = cv2.imread(img.temporary_file_path())

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
	print(count)
	# cv2.imshow('contours',image)
	# cv2.waitKey(0)

	# adds the green outlines to the original image
	cv2.drawContours(img,output,-1,(0,200,0),10)
	os.chdir("./puzzle_pieces/temp_image")
	cv2.imwrite("outlines.jpg", img)
	# cv2.imshow("window", cv2.resize(img,(int(img.shape[1]/3),int(img.shape[0]/3))))
	# cv2.waitKey(0)

	with open("outlines.jpg", "rb") as image_file:
		encoded_string = base64.b64encode(image_file.read())

	data = {
		"count": count,
		"imgData": encoded_string
	}
	return JsonResponse(data)
	
def showImage(request):
	try:
		with open("./puzzle_pieces/temp_image/outlines.jpg", "rb") as f:
			return HttpResponse(f.read(), content_type="image/jpeg")
	except IOError:
		error = {
			"error": "can't open image"
		}
		return JsonResponse(error)
