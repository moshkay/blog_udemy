import os
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from django.conf import settings
from .models import Post, Category, PostFeed, Comment, Like, Newsletter
from django.contrib.auth.models import User, auth
from django.contrib.auth import login as auth_log
from django.contrib.auth import authenticate
from django.db.models import Q
import smtplib
from email.message import EmailMessage
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
# Create your views here.




def sendMail(content):
  
    query = Newsletter.objects.all()
    test_email = []
    
    for i in query:
        test_email.append(i.email)
    
    
    test_email = test_email
    to = test_email
    subject = 'hello world'
    sent_from = settings.EMAIL_HOST_USER
    #html_content = render_to_string("etemp.html", {'content':content})
    #text_content = strip_tags(html_content)
    html_content = content
    text_content = strip_tags(html_content)
    email = EmailMultiAlternatives(
        subject,text_content,sent_from,['logiiktek@gmail.com']
    )

    email.attach_alternative(html_content, "text/html")
    #with open(os.path.join(settings.BASE_DIR, 'templates/etemp.html')) as f:
        #etemp = f.read()

    try:
        email.send()
        print('Email sent!')
    except Exception as e:
        print(e)
        print('Something went wrong...')

def emails(request):
    #sendMail()
    query = Newsletter.objects.all()
    

    context = {

        'query':query
    }

    if request.method == "POST":

        content = request.POST['content']

        sendMail(content)


        return render(request, 'emails.html')


    return render(request, 'emails.html', context)



def index(request):
    info = Post.objects.order_by('-id')
    featured = Post.objects.filter(featured = True).order_by('-id')
    first = featured[0]
    feat = Post.objects.filter(featured = True).count()
    print(feat)
    print(first)

    context = {
        'info':info,
        'featured':featured,
        'feat':feat,
        'first':first
    }

    return render(request,'home.html', context)

def sub(request):

    print('sub')
    if request.method=="POST":
        email = request.POST['email']
        newsletter = Newsletter(email=email)
        newsletter.save()
        print('sub')


        return redirect('/')

    else:
        return redirect('/')

def detail(request, id):

    if request.method=="GET":
        post = get_object_or_404(Post, pk=id)
        post.views = post.views + 1
        post.save()
        comment = Comment.objects.filter(post=post).order_by('-id')
        likes = Like.objects.all().filter(post=post).count()
        
        context = {
        'post':post,
        #'feed':feed,
        'comment':comment,
        'likes':likes,
        }


        return render(request, 'post-details.html', context)

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
            'feed':feed,
            'comment':comment,
            }

            
        else:
            return render(request, 'detail.html', {"message":'Please enter comment'})




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

def register(request):
    if request.method =="POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        password2 = request.POST["password2"]


        if password == password2:
            if User.objects.filter(username=username).exists():
                print('username taken')
                return render(request, 'login-signup.html',{'message':"username taken"})
            elif User.objects.filter(email=email).exists():
                print('email already exists')
                return render(request, 'login-signup.html',{'message':"email already exist"})
            elif len(password)<8:
                print('password too short')
                return render(request, 'login-signup.html',{'message':"Password too short"})
            elif  password.isdigit() or password.isalpha():
                print('password must contain alphanumeric characters',password)
                return render(request, 'login-signup.html',{'message':"Password must contain alphanumeric characters"})
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            print('user created')
            print(password)
            print(len(password))
            return redirect('sign')
        else:
            print('invalid password')
            message = "Password do not match"
            context = {
                'message':message,
            }
            return render(request, 'login-signup.html',context)

    else:
        return render(request, 'login-signup.html')


def logout(request):
    auth.logout(request)
    return redirect('login')


def search(request):

    
    query = request.GET.get('q')
    

    if query:


        result = Post.objects.filter(Q(title__icontains=query)|Q(content__icontains = query))

        context = {

            'result':result,
        
        }

        return render(request, 'search.html', context)

    else:

        context = {
            'cat':cat,
        }

        return render(request, 'search.html', context)


def sign(request):
    if request.user.is_authenticated:
        return redirect('/')
    
    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(username=username,password=password)
        
        if user is not None:
            auth_log(request, user)
            return redirect('/')
        else:
            context={'username':username,'password':password, 'message':"Invalid Username or Password"}
            return render(request,'login-signup.html', context)

    else:
        return render(request, 'login-signup.html')


    return render(request, 'login-signup.html')

def logout(request):
    auth.logout(request)
    return redirect('sign')


def category(request, id):
    cat = get_object_or_404(Category, pk=id)
    post = Post.objects.all().filter(category=cat)
    
    category = Category.objects.filter(id=id)
    for i in category:

        print(i.name, i.image)
    context = {

        'category':category,
        'post': post,
        
        }

    

    return render(request, 'cats.html', context)