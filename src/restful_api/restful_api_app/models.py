from django.db import models
# Base Djando user model.
from django.contrib.auth.models import AbstractBaseUser
# Assings specific persmissions to users.
from django.contrib.auth.models import PermissionsMixin
# Base user manager
from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager):

   def create_user(self, email, name, password = None):
      
      if not email:
         raise ValueError('Please provide an email address')

      email = self.normalize_email(email)

      # Create a new user profile.
      user = self.model(email = email, name = name)

      # This will encrypt the password first and then assign it to the user.
      user.set_password(password)

      # Save user into database.
      user.save(using = self._db)

      return user
   
   def create_superuser(self, email, name, password = None):

      user = self.create_user(email, name, password)
      user.is_superuser = True
      user.is_staff = True

      # Save user into database.
      user.save(using = self._db)

      return user

class User(AbstractBaseUser, PermissionsMixin):

   email = models.EmailField(max_length=255, unique = True)
   name = models.CharField(max_length = 255)
   is_active = models.BooleanField(default = True)
   is_staff = models.BooleanField(default = False)

   objects = UserManager()

   USERNAME_FIELD = 'email'
   REQUIRED_FIELDS = ['name']

   def get_full_name(self):
      return self.name 

   def get_short_name(self):
      return self.name 
   
   def __str__(self):
      # Convert the object to a string.
      return self.email
