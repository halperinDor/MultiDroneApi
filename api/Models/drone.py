from django.db import models


class Drone(models.Model):
    name = models.CharField(max_length=32,unique=True, default="")
    connect = models.BooleanField()
    bat = models.FloatField()
    fix = models.IntegerField()
    num_sat = models.IntegerField()
    lat = models.FloatField()
    lng = models.FloatField()
    alt = models.FloatField()
    zspeed = models.FloatField()
    gspeed = models.FloatField()
    heading = models.IntegerField()
    pitch = models.FloatField()
    roll = models.FloatField()
    arm = models.BooleanField()
    armable = models.BooleanField()
    ekf = models.BooleanField()
    mode = models.CharField(max_length=32)
    mission = models.CharField(max_length=32)

