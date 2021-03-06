from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from .models import Drone, Command


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
        model = Command
        fields = ('id', 'name', 'Command', 'alt')
