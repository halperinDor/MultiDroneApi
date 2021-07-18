from django.contrib import admin
from .models import Drone, DroneCommand, DroneMission

# Register your models here.
admin.site.register(Drone)
admin.site.register(DroneCommand)
admin.site.register(DroneMission)