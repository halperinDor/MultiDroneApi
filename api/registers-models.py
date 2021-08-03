from django.contrib import admin

from api.Models.drone import Drone
from api.Models.droneCommmand import DroneCommand
from api.Models.droneMission import DroneMission

# Register your models here.
admin.site.register(Drone)
admin.site.register(DroneCommand)
admin.site.register(DroneMission)

