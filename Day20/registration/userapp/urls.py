__author__ = 'abhishekrathore'


from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^users/', views.getuser),
    url(r'^register/', views.setuser),
    url(r'^form/', views.showform),

]
