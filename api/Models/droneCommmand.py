from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class DroneCommand(models.Model):
    name = models.CharField(max_length=20, default="")
    command = models.CharField(max_length=20, default="")
    alt = models.FloatField(default=0, validators=[
            MaxValueValidator(100),
            MinValueValidator(0)
        ])

