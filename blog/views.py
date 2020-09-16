from django.shortcuts import render, HttpResponse

# Create your views here.


def home(request):
    return HttpResponse("Hello")


def alone(request):
    return HttpResponse("Hello Blogpost")
