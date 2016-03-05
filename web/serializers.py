# coding: utf-8

from .models import Sensor
from rest_framework import serializers

class TodoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Sensor
        fields = ('bid', 'x_int', 'y_int', 'z_int', 'timestamp')
