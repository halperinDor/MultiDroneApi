from django.contrib import admin
from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from .views import DroneViewSet, CommandViewSet, UserViewSet, MissionViewSet, MissionsCoordinatesViewSet

router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('drones', DroneViewSet)
router.register('commands', CommandViewSet)
router.register('missions', MissionViewSet)
router.register('missionsCoordinates', MissionsCoordinatesViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
