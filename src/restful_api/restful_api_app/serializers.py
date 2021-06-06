from rest_framework import serializers

""" Used for parsing incoming request data """
class HelloSerializer(serializers.Serializer):

   name = serializers.CharField(max_length = 10)