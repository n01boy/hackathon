# coding: utf-8
from django.db import models

class Sensor(models.Model):
    bid = models.CharField(max_length=50)
    int_x = models.IntegerField()
    int_y = models.IntegerField()
    int_z = models.IntegerField()
    timestamp = models.DateTimeField()

    def __unicode__(self):
        return bid

