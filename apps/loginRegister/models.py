from __future__ import unicode_literals
from django.db import models
from django.core.exceptions import ValidationError
# Create your models here.
def validateUsername(username):
    print("validating username")
    if len(username)<8:
        raise ValidationError("username must be longer than 8")
def validatePassword(password):
    if len(password)<8:
        raise ValidationError("password must be longer than 8")
class User(models.Model):
    username = models.CharField(max_length=45,validators=[validateUsername])
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=255,validators=[validatePassword])

