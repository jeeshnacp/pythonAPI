from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class Login(AbstractUser):
    is_doctor=models.BooleanField(default=False)
    is_user=models.BooleanField(default=False)
    name=models.CharField(max_length=50,null=True)
    age=models.CharField(max_length=50,null=True)
    contact_no=models.CharField(max_length=50,null=True)
    address=models.TextField(null=True)
    gender=models.CharField(max_length=50,null=True)


# class school(models.Model):
#     name=models.CharField()