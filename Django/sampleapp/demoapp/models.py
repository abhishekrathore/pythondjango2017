from django.db import models

# Create your models here.

class Person(models.Model):
    name = models.CharField(null=False,max_length=50)
    age = models.IntegerField(null=False)

    def __str__(self):
        return self.name
