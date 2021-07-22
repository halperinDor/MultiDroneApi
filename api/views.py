from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .Models.drone import Drone
from .Models.droneCommmand import DroneCommand
from .Models.droneMission import DroneMission
from .Models.missionsCoordinates import MissionsCoordinates
from .serializers import DroneSerializer, UserSerializer, CommandSerializer, MissionSerializer
from .serializers import MissionsCoordinatesSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class DroneViewSet(viewsets.ModelViewSet):
    queryset = Drone.objects.all()
    serializer_class = DroneSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)


class CommandViewSet(viewsets.ModelViewSet):
    queryset = DroneCommand.objects.all()
    serializer_class = CommandSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)


class MissionViewSet(viewsets.ModelViewSet):
    queryset = DroneMission.objects.all()
    serializer_class = MissionSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)


class MissionsCoordinatesViewSet(viewsets.ModelViewSet):
    queryset = MissionsCoordinates.objects.all()
    serializer_class = MissionsCoordinatesSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)