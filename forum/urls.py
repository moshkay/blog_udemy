from django.urls import path
from . import views
from django.contrib.auth.views import PasswordResetView,PasswordResetDoneView,PasswordResetConfirmView,PasswordResetCompleteView

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
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('logout', views.logout, name='logout'),
    path('category/<int:id>/', views.category, name='category'),
    path('password-reset/',PasswordResetView.as_view(template_name='forgot_password.html'), 
    name="password_reset"),
    
    path('password-reset/done/',PasswordResetDoneView.as_view(template_name='password_reset_done.html'), 
    name="password_reset_done"),
    
    path('password-reset-confirm/<uidb64>/<token>/',PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), 
    name="password_reset_confirm"),
    
    path('password-reset-complete/',PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), 
    name="password_reset_complete"),
    
]