from django.contrib import admin

from .models import Person,Address
# Register your models here.

admin.site.register(Person)
admin.site.register(Address)
