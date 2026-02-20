from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Cutomer_register(models.Model):
    username=models.CharField(max_length=100,unique=True)
    email_id=models.EmailField(max_length=250,unique=True)
    phone_number = models.CharField(max_length=15,unique=True)
    password=models.CharField(max_length=15)


    def __str__(self):
        return self.username

