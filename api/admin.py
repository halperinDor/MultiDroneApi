from django.contrib import admin
from .Models.drone import Drone
from .Models.droneCommmand import DroneCommand
from .Models.droneMission import DroneMission
from .Models.missionsCoordinates import MissionsCoordinates

# Register your models here.
admin.site.register(Drone)
admin.site.register(DroneCommand)
admin.site.register(DroneMission)
admin.site.register(MissionsCoordinates)