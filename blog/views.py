from django.shortcuts import render, HttpResponse
from blog.models import Post
# Create your views here.


def home(request):
    everypost = Post.objects.all()
    return render(request, 'blog/home.html', {'everypost': everypost})


def blogpost(request, slug):
    post = Post.objects.filter(slug=slug).first()
    return render(request, 'blog/post.html', {'post': post})
