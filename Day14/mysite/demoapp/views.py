from django.shortcuts import render
from .models import Person
# Create your views here.

from django.http import HttpResponse

def demo(request):
    people = Person.objects.filter()
    context = {"crowd":people,"title":"demo page"}
    return render(request,"person.html",context)

def create(request):
    print(request.POST.get('first'),request.POST.get('last'))
    p1 = Person()
    p1.first_name = request.POST.get('first')
    p1.last_name = request.POST.get('last')
    p1.save()
    return HttpResponse("Person created successfully")

def test(request):
    html = "<html><body>Hello World</body></html>"
    return HttpResponse(html)