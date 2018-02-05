from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .models import Person
from .form import NameForm
from django.views.generic import ListView
from django.views.generic.edit import CreateView


import json

# Create your views here.



class PersonListView(ListView):
    model = Person
    template_name = 'list.html'
    context_object_name = 'person_list'

class PersonCreate(CreateView):
     model = Person
     fields = ['name','age']
     template_name = "create.html"
     success_url = '/demo/index/'




def index(request):
    person = Person.objects.all()
    # print(person[0])
    context = {"person":person}
    print(request.user.username)
    return render(request,'home.html',context)

def chats(request):
    context = {}
    if request.user.username:
        print(request.user.username)
        context ={"username": request.user.username}
        return render(request,'chats.html',context)
    else:
        return redirect('signupform')



@csrf_exempt
def submit(request):
    print(request.POST)
    p = Person()
    p.name = request.POST.get('name')
    p.age = request.POST.get('age')
    p.save()
    return redirect('index')

def getperson(request):
    person = Person.objects.all()
    people = []
    for p in person:
        people.append({"name":p.name,"age":p.age,"id":p.id})
    return JsonResponse({"people":people})


def signupform(request):
    return render(request,'signup.html')

@csrf_exempt
def signup(request):
    username = request.POST.get('email')
    password = request.POST.get('password')
    email = request.POST.get('email')
    user = User.objects.create_user(username, email, password)
    login(request,user)
    return redirect('chats')

def loginform(request):
    return render(request,'login.html')

@csrf_exempt
def loginfx(request):
    username = request.POST.get('email')
    password = request.POST.get('password')
    user = authenticate(username=username, password=password)
    login(request,user)
    return redirect('chats')


def formtest(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        print(form)
        if form.is_valid:
            # p = PersonForm(request.POST)
            # p.save()
            print(2)
        else:
            render(request, 'formtest.html', {'form':form,"is_invalid":True})

        return redirect('chats')
    else:
        form = NameForm()

    return render(request, 'formtest.html', {'form':form})


