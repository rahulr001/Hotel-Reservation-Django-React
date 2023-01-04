from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser, PermissionsMixin

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password1','password2' )
