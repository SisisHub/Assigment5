from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=50)
    age = models.FloatField()
    address = models.CharField(max_length=50)


    def __str__(self):
        return self.name + ' ' + self.address

class Offer(models.Model):
    code = models.CharField(max_length=10)
    description = models.CharField(max_length=255)
    price = models.FloatField()