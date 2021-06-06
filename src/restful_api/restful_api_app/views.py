from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import serializers

# Create your views here.

class helloApiView(APIView):

   # Tell DJando which serializer we'll be using for this endpoint.
   serializer_class = serializers.HelloSerializer

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

   def post(self, request):
      serializer = serializers.HelloSerializer(data = request.data)

      if serializer.is_valid():
         name = serializer.data.get('name')
         message = f'Hello {name}'

         return Response({'message': message})
      else:
         return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)