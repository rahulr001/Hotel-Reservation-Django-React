from django.contrib import admin
from django.urls import path, include

from rest_framework_simplejwt import views as jwt_views

from .views import  UserRegistrationView,UserAuthenticationView
app_name = 'accounts_app'

urlpatterns = [
    path('register/', UserRegistrationView.as_view()),
    path('login/', UserAuthenticationView.as_view(), name='token_obtain_pair'),
    path('refresh_token/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]

