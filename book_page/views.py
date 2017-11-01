from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from . import models
from user_page import models
# Create your views here.

def Comment(request):
    Bookname = request.POST.get('')
    Comment = models.comment.objects.all()
    abook = []
    for a_comment in Comment:
        if a_comment.bookname==Bookname:
            abook.append(a_comment)
    return JsonResponse(abook)

def NewComment(request):
    Bookname = request.POST.get('')
    Contents = request.POST.get('')
    Account = request.POST.get('')
    models.comment.objects.create(bookname=Bookname,contents=Contents,account=Account)

def Cart (request):
    Account = request.POST.get('')
    Shopping = models.ShoppingCart.objects.all()
    acart = []
    for a_shopping in Shopping:
        if Account== a_shopping.account:
            acart.append(a_shopping)
    return JsonResponse(acart)

def Buy (request):
    Account = request.POST.get('')
    BookName = request.POST.get('')
    models.ShoppingCart.objects.create(account=Account,bookname=BookName)

def Delete(request):
    Account = request.POST.get('')
    BookName = request.POST.get('')
    models.ShoppingCart.objects.filter(account=Account,bookname=BookName).delete()
