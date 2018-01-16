from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import Person
import json

# Create your views here.


def index(request):
    person = Person.objects.all()
    print(person[0])
    context = {"person":person}
    return render(request,'index.html',context)

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