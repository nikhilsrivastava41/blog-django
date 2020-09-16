from django.shortcuts import render, HttpResponse

# Create your views here.


def home(request):
    return render(request, 'blog/home.html')


def blogpost(request, slug):
    return render(request, 'blog/post.html')
