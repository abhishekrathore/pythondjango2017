from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import User


# Create your views here.

def getuser(request):
    users = User.objects.all()
    print(users)
    print(request.GET)

    names =  ""
    for user in users:
        names = names + str(user) + ","

    return HttpResponse(names)

def showform(request):

    return render(request,'register.html')

def setuser(request):

    print(request.POST)

    user = User()
    user.first_name = request.POST.get("first")
    user.age = request.POST.get("age")
    user.email = request.POST.get("email")
    user.save()


    return redirect('/userapp/users')
