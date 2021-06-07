from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken

from . import serializers
from . import models
from . import permissions

# Create your views here.

class HelloApiView(APIView):   

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

   def put(self, request, pk = None):
      """ Handles updating an object """
      return Response ({'method': 'put'})

   def patch(self, request, pk = None):

      """ Handles updating fields provided in the request """
      return Response({'method': 'patch'})

   def delete(self, request, pk = None):
      
      """ Handles deleting an object """
      return Response({'method': 'delete'})

class HelloViewSet(viewsets.ViewSet):

   # Tell DJando which serializer we'll be using for this endpoint.
   serializer_class = serializers.HelloSerializer

   def list(self, request):

      a_viewset = [
         'This is a test', 
         'We are using HTTP get method',
         'This data comes from views file using VIEWSET'
      ]

      return Response({
         'message': 'Hello from views file',
         'data':a_viewset
      })

   # POST
   def create(self, request):

      serializer = serializers.HelloSerializer(data = request.data)

      if serializer.is_valid():
         name = serializer.data.get('name')
         message = f'Hello {name}'

         return Response({'message': message})
      else:
         return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

   #GET + url param
   def retrieve(self, request, pk = None):

      """ Handles getting an object by its ID """

      return Response ({'http_method': 'get'})

   #PUT
   def update(self, request, pk = None):

      """ Handles updating an object by its ID """

      return Response ({'http_method': 'put'})
   
   #PATCH
   def partial_update(self, request, pk = None):

      """ Handles updating a part of an object by its ID """

      return Response ({'http_method': 'patch'})
   
   #DELETE
   def destroy(self, request, pk = None):

      """ Handles deleting an object by its ID """

      return Response ({'http_method': 'delete'})

class UserViewSet(viewsets.ModelViewSet):

   """ Handles creating, reading, updating and deleting  (CRUD) user profiles """
   # Tell DJando which serializer we'll be using for this endpoint.
   serializer_class = serializers.UserSerializer

   # Tells the viewset how to retrieve the objects from the database.
   queryset = models.User.objects.all()
   
   authentication_classes = (TokenAuthentication, )
   permission_classes = (permissions.UpdateOwnProfile,)
   filter_backends = (filters.SearchFilter, )
   search_fields = ('name', 'email', )

class LoginViewSet(viewsets.ViewSet):
   """ Check email and password and returns authentication token """ 
   # Tell DJando which serializer we'll be using for this endpoint.
   serializer_class = AuthTokenSerializer

   def create(self, request):

      """ Use the ObtainAuthToken APIView to validate and create a token """
      # return ObtainAuthToken().post(request)
      # ref: https://stackoverflow.com/questions/66795116/drf-obtainauthtoken-object-has-no-attribute-request
      return ObtainAuthToken().as_view()(request=request._request)
