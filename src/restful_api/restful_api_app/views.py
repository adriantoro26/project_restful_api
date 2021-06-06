from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class helloApiView(APIView):

   def get(self, request, format=None):

      an_apiview = [
         'This is a test', 
         'We are using HTTP get method',
         'This data comes from views file using APIVIEWS'
      ]

      return Response({
         'message': 'Hello from views file',
         'data':an_apiview
      })
