from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.demo1),
    url(r'^demo1/',views.demo1)
]