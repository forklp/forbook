from django.conf.urls import url
from book_page import views
urlpatterns = [
    url(r'^comment/',views.Comment),
    url(r'^cart/',views.Cart),
    url(r'^buy/',views.Buy),
    url(r'^newcomment/',views.NewComment),
    url(r'^delete/',views.Delete),

]