from django.contrib import admin
from .models import User
from .models import ShoppingCart
# Register your models here.
admin.site.register(User)
admin.site.register(ShoppingCart)