import os
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.conf import settings
from .models import Post, Category, PostFeed, Comment, Like
from django.contrib.auth.models import User, auth
# Create your views here.

def index(request):
    info = Post.objects.order_by('-id')
    context = {
        'info':info,
    }


    return render(request,'blog.html', context)


def detail(request, id):

    if request.method=="GET":
        post = get_object_or_404(Post, pk=id)
        comment = Comment.objects.filter(post=post).order_by('-id')
        likes = Like.objects.all().filter(post=post).count()
        
        context = {
        'post':post,
        #'feed':feed,
        'comment':comment,
        'likes':likes,
        }


        return render(request, 'detail.html', context)

    else:
        opinion = request.POST["opinion"]
        
        if opinion:
            post = Post.objects.get(id=id)
            comment = Comment(opinion=opinion, post=post)
            comment.save()
            post = get_object_or_404(Post, pk=id)
            comment = Comment.objects.filter(post=post).order_by('-id')
            
            
            context = {
            'post':post,
            #'feed':feed,
            'comment':comment,
            }

            return render(request, 'detail.html', context)
        else:
            return render(request, 'detail.html', {"message":'Please enter comment'})

def response(request):
    if request.method =="POST":
        reply = request.POST["reply"]
        comment = Comment.objects.get(id=reply)
        print(comment)

        return HttpResponse("done")







def like(request):
    user_id = request.user.id
    user = get_object_or_404(User, id=user_id)
    post_id = request.POST['post_id']
    post = get_object_or_404(Post, id=post_id)
    like = Like.objects.filter(user_id = user,post=post).count()

    if like < 1:
        post.likes = post.likes + 1
        post.save()

        like = Like.objects.create(post=post,likes=post.likes,user_id=user)

        return render(request, 'detail.html', {"like":like.likes})
    else:
        return render(request, 'detail.html')
        



def login(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            return render(request, 'login.html',{'message': "Invalid username or password"})
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('login')