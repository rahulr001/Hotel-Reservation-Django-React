from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.http import JsonResponse
from django.contrib.auth.models import User
from .serializers import UserSerializer

# class MyTokenObtainSerilizer(TokenObtainPairSerializer):
#     # serializer_class = TokenObtainPairSerializer
#
#     def validate(self, attrs):
#         data = super().validate(attrs)
#
#         refresh = self.get_token(self.user)
#         data['refresh'] = str(refresh)
#         data['access'] = str(refresh.access_token)
#         # Add your required response and other parameters here
#         data['username'] = self.user.username
#         data['user_id'] = self.user.pk
#         data['is_admin'] = self.user.is_staff
#         data['message'] = "login successful"
#
#         return data
#
#
# class MyTokenObtainPairView(TokenObtainPairView):
#     serializer_class = MyTokenObtainSerilizer
#
#
# class UserView(APIView):
#     parser_classes = (MultiPartParser, FormParser, JSONParser)
#
#     def post(self, request, *args, **kwargs):
#         post_data = dict(request.data)
#         user_name = User.objects.filter(username=post_data['username'])
#         if user_name.exists():
#             return Response({"response": "username already taken"}, status=status.HTTP_400_BAD_REQUEST)
#         email = User.objects.filter(email=post_data['email'])
#         if email.exists():
#             return Response({"response": "email already exists"}, status=status.HTTP_400_BAD_REQUEST)
#         if post_data['password1'] != post_data['password2']:
#             return Response({"response": "Passwords don't match"}, status=status.HTTP_400_BAD_REQUEST)
#
#         user = User.objects.create_user(
#             username=post_data['username'],
#             email=post_data['email'],
#             password=post_data['password1']
#         )
#
#         new_user = {
#             "response": "Your Registration Is Successful",
#             "id": user.id,
#             "username": user.username,
#             "email": user.email
#         }
#         user.set_password(post_data['password1'])
#         user.save()
#         return JsonResponse(new_user, status=status.HTTP_200_OK)
#

# from .authentication import EmailBackendModel
from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.core.cache import cache
from .serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# from . import request_utils
from . import models

from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model


def retrieve_email_and_password(request):
    """
        Extract the email and the password from a request
        :param request: The request
    """
    username = request.data.get('username', '')
    password = request.data.get('password', '')
    email= request.data.get('email','')
    return username, password, email


def is_user_authenticated(request):
    """
        Check if the session exist inside the specified
        request
        :param request: The request being analyzed
    """
    return request.session.session_key


def is_user_admin(request):
    """
        Check if the user is an administrator
        :param request: The request sent by the user
    """
    return request.user.is_superuser


class EmailBackendModel(ModelBackend):
    """
        Backend used to authenticate users and
        helps generate the session id
    """

    def authenticate(self, username=None, password=None,  ):
        """
            authenticate the user by retrieving it from the
            database
            :param username: The username of the user
            :param password: The password of the user
            :param kwargs: Other cool stuff you can add
        """
        UserModel = get_user_model()
        try:
            user = UserModel.objects.get(username=username)
            return user
        except UserModel.DoesNotExist:
            return None


class UserAuthenticationView(APIView):
    def post(self, request, format=None):
        username, password,email = retrieve_email_and_password(request)
        authentication_backend = EmailBackendModel()
        user = authentication_backend.authenticate(username=username, password=password)
        if user is None:
            return Response({'errors': 'The requested user does not exist'}, status=status.HTTP_400_BAD_REQUEST)
        if user.is_ban:
            return Response({'errors': 'The requested user is banned'}, status=status.HTTP_400_BAD_REQUEST)
        login(request, user)
        cache.set(request.session.session_key, user.username, 60 * 60 * 24)
        serializer = UserSerializer(user, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserRegistrationView(APIView):

    def post(self, request, format=None):

        # if is_user_authenticated(request):
        #     return Response({'errors': 'User is authenticated'}, status=status.HTTP_400_BAD_REQUEST)
        username, password,email = retrieve_email_and_password(request)

        user = User.objects.create_user(username=username,email=email, password=password)
        if not user:
            return Response({'errors': 'The username already exist'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_200_OK)
