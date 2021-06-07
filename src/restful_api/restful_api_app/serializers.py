from rest_framework import serializers
from . import models

""" Used for parsing incoming request data """
class HelloSerializer(serializers.Serializer):

   name = serializers.CharField(max_length = 10)

class UserSerializer(serializers.ModelSerializer):
   """ A serializer for user objects """

   class Meta:
      model = models.User
      fields = ('id', 'email', 'name', 'password')
      extra_kwargs = {'password':{'write_only':True}}

   def create(self, validated_data):
      """ Create and return a new user """

      user = models.User(
         email = validated_data['email'],
         name = validated_data['name']         
      )

      # This will encrypt the password first and then assign it to the user.
      user.set_password(validated_data['password'])

      # Save user into database.
      user.save()

      return user