# coding: utf-8
import json

from django.core import serializers
from django.http import HttpResponse
from django.template import loader, RequestContext
from rest_framework.viewsets import ModelViewSet

from .models import Sensor
from .serializers import SensorSerializer


class SensorViewSet(ModelViewSet):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


def dataview(req):
    device_list = serializers.serialize("json", "")
    contexts = RequestContext(req, {"device_list": device_list})
    template = loader.get_template('view.html')
    return HttpResponse(template.render(contexts))


def ajaxdataview(req):
    dbdata = getCurrencyDBData()
    bid = json.dumps(list(dbdata.values_list('bid', flat=True)))
    value_x = json.dumps(list(dbdata.values_list('value_x', flat=True)))
    value_y = json.dumps(list(dbdata.values_list('value_y', flat=True)))
    value_z = json.dumps(list(dbdata.values_list('value_z', flat=True)))
    timestamp = json.dumps(list(dbdata.values_list('timestamp', flat=True)), default=date_handler)
    response = json.dumps(
        {'bid': bid, 'value_x': value_x, 'value_y': value_y, 'value_z': value_z, 'timestamp': timestamp})
    return HttpResponse(response)


def getCurrencyDBData(reqbid=None):
    queryset = Sensor.objects.order_by("-timestamp")[:200]
    return queryset


def date_handler(obj):
    return obj.isoformat()
