from django.db import models
from django.forms import ModelForm
from django.urls import reverse

# Create your models here.



class Person(models.Model):
    name = models.CharField(null=False,max_length=50)
    age = models.IntegerField(null=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('person-create', kwargs={'pk': self.pk})


class Address(models.Model):
    person = models.ManyToManyField(Person)
    street = models.CharField(null=False,max_length=50)
    pincode = models.IntegerField(null=False)
    city = models.CharField(null=False,max_length=50)

    def __str__(self):
        return self.street


#
# class PersonForm(ModelForm):
#    class Meta:
#         model = Person
#         fields = ['name','age']
