from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import UserManager
from django.db import models


# Create your models here.
class UserModel(AbstractBaseUser):
    """
        Define the model of the user
    """
    # objects = UserManager()

    username = models.CharField(max_length=10,unique=True)
    email = models.EmailField()
