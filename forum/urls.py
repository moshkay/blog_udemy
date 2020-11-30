from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('detail/<int:id>/', views.detail, name='detail'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('like', views.like, name='like'),
    path('register', views.register, name='register'),
    path('search', views.search, name='search'),
    path('sub', views.sub, name='sub'),
    path('emails', views.emails, name='emails'),
    path('sign', views.sign, name='sign'),
    path('logout', views.logout, name='logout')
    
]