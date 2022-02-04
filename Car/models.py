from django.db import models

# Create your models here.
class Car(models.Model):
    name = models.CharField(max_length=100,null=False)
    brand = models.CharField(max_length=100,null=False)
    price = models.FloatField(max_length=10000000)

    def __str__(self):
        return self.name
