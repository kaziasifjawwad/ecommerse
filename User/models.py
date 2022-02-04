from django.db import models
from Car.models import *

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100, null=False)
    email = models.EmailField(max_length=100, null=False)
    DateOfBirth = models.DateField(null=False)
    accountCreated = models.DateField(auto_now=True)
    contactInfo = models.CharField(max_length=14)
    favouriteCar = models.ManyToManyField(to = Car)

    def __str__(self):
        return self.name
