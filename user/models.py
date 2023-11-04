from django.db import models


class UserModel(models.Model):
    fullname = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    email = models.EmailField()
    mobile = models.IntegerField()
    password = models.CharField(max_length=100)
    confirm_password = models.CharField(max_length=100)
