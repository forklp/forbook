from django.contrib import admin
from .models import Books
from .models import comment
# Register your models here.
admin.site.register(comment)
admin.site.register(Books)