from django.db import models


class DroneMission(models.Model):
    name = models.CharField(max_length=32, default="")
    coordinates = models.CharField(max_length=2000, default="")