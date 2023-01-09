from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from .models import UserModel


# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('id', 'username', 'email', 'password1', 'password2')

class UserSerializer(serializers.ModelSerializer):

    # tasks = serializers.HyperlinkedRelatedField(many=True, view_name=urls_name.TODO_DETAIL_NAME, read_only=True)

    def create(self, validated_data):
        """
            Create a new User using validated data
        """
        user_instance = UserModel.objects.create_user(**validated_data)
        user_instance.save()
        return user_instance

    def update(self, instance, validated_data):
        """
            Update values from the instance thanks to the validated_data
            coming from the request
            :param instance: The instance of the User being updated
            :param validated_data: The validated data being used as reference
            :return: The edited instance
        """
        for attr, value in validated_data.items():
            instance.set_password(value) if attr == 'password' else setattr(instance, attr, value)
        instance.save()
        return instance

    class Meta:

        model = UserModel
        fields = ('id', 'username', 'email', 'password' )
