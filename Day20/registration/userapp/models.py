from django.db import models

# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length=30)
    age = models.IntegerField(null=True)
    email = models.EmailField(null=False)

    def __str__(self):
        return self.first_name


