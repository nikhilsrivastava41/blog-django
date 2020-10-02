from django.shortcuts import render, HttpResponse, redirect
from blog.models import Post, BlogComment
# Create your views here.


def home(request):
    everypost = Post.objects.all()
    return render(request, 'blog/home.html', {'everypost': everypost})


def blogpost(request, slug):
    post = Post.objects.filter(slug=slug).first()
    comment = BlogComment.objects.filter(post=post)
    return render(request, 'blog/post.html', {'post': post, 'comment': comment, 'user': request.user})


def postcomment(request):
    if request.method == "POST":
        comment = request.POST.get("comment")
        user = request.user
        postsno = request.POST.get("postsno")
        post = Post.objects.get(sno=postsno)
        comment = BlogComment(comment=comment, user=user, post=post)
        comment.save()
    return redirect(f'/blog/{post.slug}')
