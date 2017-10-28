__author__ = 'abhishekrathore'

from django.conf.urls import url

from . import views

urlpatterns = [
        url(r'^demo', views.demo),
        url(r'^test', views.test),

]