from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateTimeField('date published')
    author = models.CharField(max_length=75)
    excerpt = models.TextField()
    body = models.TextField()