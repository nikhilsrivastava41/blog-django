from django.db import models

# Create your models here.


class Post(models.Model):
    sno = models.IntegerField()
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.CharField(max_length=100)
    timeStamp = models.DateTimeField(blank=True)
    slug = models.CharField(max_length=200)
