from django.urls import path,include

from . import views
urlpatterns = [
    path('index/', views.index, name="index" ),
    path('submit/', views.submit, name="submit"),
    path('getperson/', views.getperson, name="getperson")

    ]