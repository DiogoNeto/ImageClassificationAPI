from django.shortcuts import render
from rest_framework import viewsets
from .models import Image
from .serializers import ImageSerializer
from django.http import HttpResponse
from django.http import JsonResponse
import random
import tensorflow as tf
import face_recognition

#def helloworld(request,num1):
    #logs_path='home/dc/pyweb'

    #n1=int(num1)
    #n2=int(num2)
    #x=tf.placeholder(tf.int32)
    #y=tf.placeholder(tf.int32)

    #add=tf.add(x,y)
    #with tf.Session() as sess:
        #summary_writer = tf.summary.FileWriter(logs_path, graph=tf.get_default_graph())

        #z=sess.run(add,feed_dict={x:n1,y:n2})
    #return HttpResponse("Hello World!")

class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

def nFaces(request):    
    image = face_recognition.load_image_file("/home/diogo/django/drf-30-min/api/core/foto4.jpg")
    
    face_locations = face_recognition.face_locations(image)    
    top, right, bottom, left = face_locations[0]
    #face_image = image[top:bottom, left:right]

    face_landmarks_list = face_recognition.face_landmarks(image)

    list_of_face_encodings = face_recognition.face_encodings(image)

    responseData = {
        'Faces' : len(face_locations),
        'top' : top,
        'right' : right,
        'bottom' : bottom,
        'left' : left,
        'Landmarks' : face_landmarks_list
        
        #'ListFaceEncodings' : list_of_face_encodings
    }

    return JsonResponse(responseData)
    
# def landmarks(request):
#     image = face_recognition.load_image_file("/home/diogo/django/drf-30-min/api/core/foto3.jpg")
#     face_landmarks_list = face_recognition.face_landmarks(image)
#     return face_landmarks_list

# def xpto(request):
#     from imutils import face_utils1
#     import numpy as np
#     import argparse
#     import imutils
#     import dlib
#     import cv2

#     return ""


    #return HttpResponse("I found {} face(s) in this photograph.".format(len(face_locations)))


    #return HttpResponse("Yeah!!! %s" %(n3))


# class XPTOViewSet(viewsets.ModelViewSet):
#     queryset = XPTO.objects.all()
#     serializer_class = ClienteSerializer


# class FileUploadView(viewsets.APIView):
#      parser_classes = (FileUploadParser,)   
    
# def post(self, request, format=None):
#         logger.print("adsad")
#         serializer = SnippetSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# def put(self, request, format=None):
#         logger=("Test")
#         serializer = SnippetSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def post(self, request, format=None):
    #     file_obj = request.data['file']

    #     print("aaa")
    #     # ...
    #     # do some stuff with uploaded file
    #     # ...
    #     return HttpResponse(status=204)
