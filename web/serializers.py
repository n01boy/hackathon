# coding: utf-8

from .models import Sensor
from rest_framework import serializers

class SensorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Sensor
        fields = ('bid', 'value_x', 'value_y', 'value_z', 'timestamp')
