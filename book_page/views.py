from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from . import models
from user_page import models
# Create your views here.

def Comment(request):
    Bookname = request.POST.get('')
    Comment = models.comment.objects.all()
    for a_comment in Comment:
        if a_comment.bookname==Bookname:
            return HttpResponse(a_comment.contents)
    return HttpResponse(0)

def Cart (request):
    Account = request.POST.get('')
    Shopping = models.ShoppingCart.objects.all()
    for a_shopping in Shopping:
        if Account== a_shopping.account:
            return HttpResponse(a_shopping)
    return HttpResponse(0)

def Buy (request):
    Account = request.POST.get('')
    BookName = request.POST.get('')
    if list(models.ShoppingCart.objects.filter(account=Account)):
        Name = models.ShoppingCart.objects.get(account=Account)
        Name.bookname = BookName
        Name.save()
        return HttpResponse(1)
    else :
        models.ShoppingCart.objects.create(account=Account,bookname=BookName)
        return HttpResponse(1)
    return HttpResponse(0)
