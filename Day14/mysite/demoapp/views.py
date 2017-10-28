from django.shortcuts import render
from .models import Person
# Create your views here.

from django.http import HttpResponse

def demo(request):
    people = Person.objects.filter()
    # html = "<table>"
    # for p in people:
    #     html += "<tr><td>" +p.first_name +"</td></tr>"
    # html += "</table>"

    print(people)
    context = {"crowd":people,"title":"demo page"}
    return render(request,"person.html",context)


def test(request):
    html = "<html><body>Hello World</body></html>"
    return HttpResponse(html)