
from django.conf.urls import url
from user_page import views

urlpatterns = [
    url(r'^vercode/', views.MyVerVode),
    url(r'^login/', views.MyLogin),
    url(r'^register/', views.MyRegister),
    url(r'^personal/', views.PersonalInformation),
    url(r'^modifipersonal/', views.ModifiPersonal),

]