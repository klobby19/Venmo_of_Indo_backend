from django.db import models

class User(models.Model):
    name = models.CharField(max_length=60)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=60)
    phonenumber = models.CharField(max_length=20)
    email = models.CharField(max_length=60)
    def __str__(self):
        return self.name
