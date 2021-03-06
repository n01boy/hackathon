"""linking URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter
from web import views

router = DefaultRouter()
router.register(r'sensor', views.SensorViewSet)

urlpatterns = [
    url(r'^linking/', include(router.urls)),
    url(r'^admin/', admin.site.urls),
    url(r'^dashboard','web.views.dataview'),
    url(r'^api/linking/sensor','web.views.ajaxdataview')
]
