from django.shortcuts import render, HttpResponse
from home.models import Contact
from django.contrib import messages
from blog.models import Post
# Create your views here.


def home(request):
    return render(request, 'home/home.html')


def about(request):
    return render(request, "home/about.html")


def contact(request):

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']
        if len(name) <= 0 or len(email) <= 5 or len(phone) < 10 or len(content) < 1:
            messages.error(request, "One of the fields not filled correctly")
        else:
            messages.success(request, 'Issue submitted successfully!')
            contact = Contact(name=name, email=email,
                              phone=phone, content=content)
            contact.save()
    return render(request, "home/contact.html")


def search(request):
    search = request.GET['search']
    everypost = Post.objects.filter(title__icontains=search)
    return render(request, 'home/search.html', {'everypost': everypost})
