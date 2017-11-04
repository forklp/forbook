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
    dict1 = {}
    dict2 = {}
    list = range(100)
    i = 0
    dict2['account'] = d.account
    dict2['password'] = d.password
    dict1[list[i]] = dict2
    return JsonResponse(dict1)
    return render(request,'demos/demo1.html',dict2)


    #return render(request, 'demos/demo1.html', a)
