from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from .Models.drone import Drone
from .Models.droneCommmand import DroneCommand
from .Models.droneMission import DroneMission
from .Models.missionsCoordinates import MissionsCoordinates


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user


class DroneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drone
        fields = ('id', 'name', 'connect', 'bat', 'fix', 'num_sat', 'lat',
                  'lng', 'alt', 'zspeed', 'gspeed', 'heading', 'pitch', 'roll', 'arm', 'armable',
                  'ekf', 'mode', 'mission')


class CommandSerializer(serializers.ModelSerializer):
    class Meta:
        model = DroneCommand
        fields = ('id', 'name', 'command', 'alt')


class MissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DroneMission
        fields = ('id', 'name','alt', 'coordinates')


class MissionsCoordinatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = MissionsCoordinates
        fields = ('id', 'missions')