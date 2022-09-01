from xml.etree.ElementInclude import include
from django.urls import path
from Appinicio import views


urlpatterns = [
    path('', views.inicio)
]