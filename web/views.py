# coding: utf-8
from django.shortcuts import render


from rest_framework.viewsets import ModelViewSet
from .models import Sensor
from .serializers import SensorSerializer

class SensorViewSet(ModelViewSet):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer
