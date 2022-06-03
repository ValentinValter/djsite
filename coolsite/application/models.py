from django.db import models


class Car(models.Model):
    Name = models.CharField(max_length=50)
    Colour = models.CharField(max_length=50)
    Odo = models.IntegerField(default=0)
