
from django.conf.urls import url
from user_page import views

urlpatterns = [
    url(r'^register/', views.MyRegister),
    url(r'^login/', views.MyLogin),

]