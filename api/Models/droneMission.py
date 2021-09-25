from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class DroneMission(models.Model):
    name = models.CharField(max_length=32, default="")
    alt = models.FloatField(default=0, validators=[
        MaxValueValidator(100),
        MinValueValidator(0)
    ])
    coordinates = models.CharField(max_length=2000, default="")
