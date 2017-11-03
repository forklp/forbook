from django.contrib import admin
from .models import User
from .models import ShoppingCart
# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ('account','password','pub_time')
    list_filter = ('pub_time',)

class ShoppigCartAdmin(admin.ModelAdmin):
    list_display = ('bookname','account','pub_time')
    list_filter = ('pub_time',)
admin.site.register(User,UserAdmin)
admin.site.register(ShoppingCart,ShoppigCartAdmin)