from django.contrib import admin
from .models import Drone, Command

# Register your models here.
admin.site.register(Drone)
admin.site.register(Command)