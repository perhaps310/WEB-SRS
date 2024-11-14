from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class  User(AbstractUser):
    email =  models.EmailField(max_length=255, unique=True)
    username =  models.CharField(max_length=255, unique=True)
    password =   models.CharField(max_length=255)
    role =  models.CharField(max_length=255, choices=[('admin', 'admin'), ('user', 'user')])
    firstname =   models.CharField(max_length=255)
    lastname =    models.CharField(max_length=255)






