from __future__ import unicode_literals
from ..loginRegister.models import User 
from django.db import models

# Create your models here.
class Forum(models.Model):
    forum = models.CharField(max_length=45)
    description = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Thread(models.Model):
    thread = models.CharField(max_length=255)
    forum = models.ForeignKey(Forum)
    creator = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Post(models.Model):
    post = models.TextField()
    thread = models.ForeignKey(Thread)
    writer = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
