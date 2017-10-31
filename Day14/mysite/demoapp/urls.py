__author__ = 'abhishekrathore'

from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
        url(r'^demo', views.demo),
        url(r'^test', views.test),
        url(r'^create$', views.create),


]
