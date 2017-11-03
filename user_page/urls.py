
from django.conf.urls import url
from user_page import views

urlpatterns = [
    url(r'^vercode/', views.MyVerVode),
    url(r'^login/', views.MyLogin),
    url(r'^modifiaccount/', views.ModifiAccount),
    url(r'^modifipassword/', views.ModifiPassword),

]