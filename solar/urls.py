from django.conf.urls import url

from solar import views

urlpatterns = [
    url(r'^workstation$', views.workstation, name='workstation'),
    url(r'^products$', views.products, name='products'),
]
