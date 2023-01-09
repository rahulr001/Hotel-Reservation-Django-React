from django.contrib.auth import login
from django.contrib.auth.models import User
from django.core.cache import cache
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from .serializers import UserSerializer


def retrieve_email_and_password(request):
    username = request.data.get('username')
    password = request.data.get('password1')
    email = request.data.get('email')
    print(username, password, email)
    return username, password, email


class UserAuthenticationView(APIView):

    def post(self, request, format=None):
        username = request.data.get('username')
        password = request.data.get('password1')
        print(username, password)
        user = authenticate(username=username, password=password)
        if user is None:
            return Response({'errors': 'The requested user does not exist'}, status=status.HTTP_400_BAD_REQUEST)
        login(request, user)
        serializer = UserSerializer(user, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserRegistrationView(APIView):

    def post(self, request, format=None):
        username, password, email = retrieve_email_and_password(request)

        user = User.objects.create_user(username=username, email=email, password=password)
        if not user:
            return Response({'errors': 'The username already exist'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_200_OK)
