from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
# Create your models here.


class Post(models.Model):
    sno = models.IntegerField()
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.CharField(max_length=100)
    timeStamp = models.DateTimeField(blank=True)
    slug = models.CharField(max_length=200)


class BlogComment(models.Model):
    sno = models.AutoField(primary_key=True)
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    timeStamp = models.DateTimeField(default=now)
