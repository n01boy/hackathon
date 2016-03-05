# coding: utf-8
from django.db import models

class Sensor(models.Model):
    bid = models.CharField(max_length=50)
    value_x = models.FloatField()
    value_y = models.FloatField()
    value_z = models.FloatField()
    timestamp = models.DateTimeField()

    def __unicode__(self):
        return bid
