from django.conf.urls import url
from solarDesign import views

app_name = 'greenesto'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^calculator/$', views.calculator, name='calculator'),
]
