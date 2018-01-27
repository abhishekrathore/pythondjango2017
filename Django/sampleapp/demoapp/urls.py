from django.urls import path,include

from . import views
urlpatterns = [
    path('index/', views.index, name="index" ),
    path('chats/', views.chats, name="chats" ),
    path('submit/', views.submit, name="submit"),
    path('getperson/', views.getperson, name="getperson"),
    path('signupform/', views.signupform, name="signupform"),
    path('signup/', views.signup, name="signup"),
    path('loginform/', views.loginform, name="loginform"),
    path('login/', views.loginfx, name="login")
    ]