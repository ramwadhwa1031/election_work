from django.db import models

# Create your models here.

class Post(models.Model):
    Post_Type = (
        ('a', 'a'),
        ('b', 'b'),
        ('c', 'c'),
    )
    name  = models.CharField(max_length=200, default='')
    post  = models.CharField(max_length= 30, choices = Post_Type)
    phone = models.CharField(max_length=10 , default='')
    opid    = models.CharField(max_length=20, default='')
