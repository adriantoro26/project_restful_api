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

class FeedItemSerializer(serializers.ModelSerializer):
   """ A serializer for feed objects """

   class Meta:
      model = models.FeedItem
      fields = ('id', 'user_profile', 'status_text', 'created_on')
      # This makes sure that users don't create feed items for other users in the system.
      # Therefore we'll create feed items for the currently logged in user.
      extra_kwargs = {'user_profile':{'read_only':True}}