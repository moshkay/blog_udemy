from django.contrib import admin
from .models import Category, Post, PostFeed, Comment, Newsletter

# Register your models here.


class PostFeedAdmin(admin.StackedInline):
    model = PostFeed    


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    
    inlines = [PostFeedAdmin]

    class Meta:
        model = Post


@admin.register(PostFeed)
class PostFeedAdmin(admin.ModelAdmin):
    pass

admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Newsletter)