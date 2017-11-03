from django.contrib import admin
from .models import Books
from .models import comment
# Register your models here.
class commentAdmin(admin.ModelAdmin):
    list_display = ('account','contents','pub_time')
    list_filter = ('pub_time',)

class BooksAdmin(admin.ModelAdmin):
    list_display = ('bookname','number','pub_time')
    list_filter = ('pub_time',)
admin.site.register(comment,commentAdmin)
admin.site.register(Books,BooksAdmin)