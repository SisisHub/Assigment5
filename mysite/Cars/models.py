from django.db import models


class Car(models.Model):
    make = models.CharField(max_length=50)
    carmodel = models.CharField(max_length=50)
    year = models.IntegerField()
    location = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    #image_url = models.CharField(max_length=2083)


    def __str__(self):
        return self.make + ' ' + self.carmodel

