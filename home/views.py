from django.shortcuts import render, HttpResponse, redirect
from home.models import Contact
from django.contrib import messages
from blog.models import Post
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
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
    everyposttitle = Post.objects.filter(title__icontains=search)
    everypostcontent = Post.objects.filter(content__icontains=search)
    everypost = everyposttitle.union(everypostcontent)
    if len(everypost) == 0:
        messages.warning(request, "Please refine your query")
    return render(request, 'home/search.html', {'everypost': everypost})


def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        password = request.POST['password']
        if not username.isalnum():
            messages.error(
                request, "Usename should by consisting of only numbers or characters")
            return redirect('home')
        user = User.objects.create_user(username, email, password)
        user.first_name = fname
        user.last_name = lname
        user.save()
        messages.success(request, "User created successfully")
        return redirect('home')
    else:
        return HttpResponse("404 Not Found")


def handlelogin(request):
    if request.method == "POST":
        uname = request.POST['uname']
        pass1 = request.POST['pass1']
        user = authenticate(username=uname, password=pass1)
        if user is not None:
            login(request, user)
            messages.success(request, "Logged in successfully")
            return redirect('home')
        else:
            messages.error(request, "Wrong credentials, please try again")
            return redirect('home')

    return HttpResponse("404 Not Found")


def handlelogout(request):
    logout(request)
    messages.success(request, "Logged out successfully")
    return redirect('home')
