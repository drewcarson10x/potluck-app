from django.db import models

class User(models.Model):
    firstname = models.CharField(max_length=32)
    lastname = models.CharField(max_length=32)
    username = models.CharField(max_length=32)
    dob = models.DateField()
    bio = models.CharField(max_length=200)