from django.http import HttpResponse
from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from user_page import models
from django.template import Template, Context
import json
# Create your views here.
def demo1(request):
    d= models.User.objects.get(account='klp')
    a = [1,2,3]
    return render(request,'demos/demo1.html',a)


    #return render(request, 'demos/demo1.html', a)
