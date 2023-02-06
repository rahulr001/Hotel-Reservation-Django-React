from django.contrib.auth import get_user_model
# from .authentication import EmailBackendModel
from django.contrib.auth import login
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User
from django.core.cache import cache
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import   authenticate
from .serializers import UserSerializer



def retrieve_email_and_password(request):
    """
        Extract the email and the password from a request
        :param request: The request
    """
    username = request.data.get('username')
    password = request.data.get('password1')
    email = request.data.get('email')
    print(username,password,email)
    return username, password, email





class EmailBackendModel(ModelBackend):
    """
        Backend used to authenticate users and
        helps generate the session id
    """

    def authenticate(self, username=None, password=None, ):
        """
            authenticate the user by retrieving it from the
            database
            :param username: The username of the user
            :param password: The password of the user
            :param kwargs: Other cool stuff you can add
        """
        User = get_user_model()
        try:
            user = User.objects.get(username=username)
            return user
        except User.DoesNotExist:
            return None


class UserAuthenticationView(APIView):

    def post(self, request, format=None):
        username = request.data.get('username')
        password = request.data.get('password1')
        print(username,password)
        user = authenticate(username=username, password=password)
        if user is None:
            return Response({'errors': 'The requested user does not exist'}, status=status.HTTP_400_BAD_REQUEST)
        login(request, user)
        # cache.set(request.session.session_key, user.username, 60 * 60 * 24)
        serializer = UserSerializer(user, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserRegistrationView(APIView):

    def post(self, request, format=None):
        # if is_user_authenticated(request):
        #     return Response({'errors': 'User is authenticated'}, status=status.HTTP_400_BAD_REQUEST)
        username, password, email = retrieve_email_and_password(request)

        user = User.objects.create_user(username=username, email=email, password=password)
        if not user:
            return Response({'errors': 'The username already exist'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'response':'Successfully registered'},status=status.HTTP_200_OK)
