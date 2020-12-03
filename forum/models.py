
from django.conf import settings
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User

# Create your models here.



class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to = 'pics', null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return str(self.name)

class Post(models.Model):
    title = models.CharField(max_length = 200)
    content = RichTextUploadingField(null=True, blank=True)
    content2 = RichTextUploadingField(null=True, blank=True)
    image = models.ImageField(upload_to = 'pics',null = True)
    date_created = models.DateTimeField(auto_now=True)
    date_updated = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True,blank=True)
    #like = models.ManyToManyField('Like', related_name='like', blank=True)
    likes = models.IntegerField(default=0)
    featured = models.BooleanField(default='False')
    live = models.BooleanField(default='False')
    views = models.IntegerField(default=0)
    audio = models.FileField(upload_to='pics', null=True,blank=True )
    video = models.FileField(upload_to='pics', null=True, blank=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.title


class PostFeed(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,null=True,blank=True)
    feed = RichTextUploadingField(null=True, blank=True)
    

class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,null=True,blank=True)
    reply = models.ForeignKey('self', null=True, related_name='replies', on_delete=models.CASCADE, blank=True)
    opinion = models.TextField()
    date_created = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE, null=True)

class Like(models.Model):
    likes = models.IntegerField()
    post = models.ForeignKey(Post,on_delete=models.CASCADE,null=True,blank=True)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)



class Newsletter(models.Model):

    email = models.EmailField()

    def __str__(self):
        return self.email

class Contact(models.Model):
    email = models.EmailField(null=True,blank=True)
    message = models.TextField(max_length=500,null=True,blank=True)
    email_sent = models.CharField(max_length=10,default='no')
    date_created = models.DateTimeField(auto_now=True)

