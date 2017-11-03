from django.shortcuts import render
from django.template import Template, Context
from django.http import HttpResponse, JsonResponse
from . import models
from user_page import models
# Create your views here.

def Comment(request):
    Bookname = request.POST.get('bookname','Bookname')
    #Comment = models.comment.objects.all()
    # abook = []
    # for a_comment in Comment:
    #     if a_comment.bookname==Bookname:
    #         abook.append(a_comment)
    # return JsonResponse(abook)
    abook = models.comment.objects.filter(bookname=Bookname)
    return render(request,'/book_page/comment.html',Context(abook))


def NewComment(request):
    Bookname = request.POST.get('bookname','Bookname')
    Contents = request.POST.get('contents','Contents')
    Account = request.POST.get('account','Account')
    models.comment.objects.create(bookname=Bookname,contents=Contents,account=Account)
    return HttpResponse(1)

def Cart (request):
    Account = request.POST.get('account','Account')
    # Shopping = models.ShoppingCart.objects.all()
    # acart = []
    # for a_shopping in Shopping:
    #     if Account== a_shopping.account:
    #         acart.append(a_shopping)
    # return JsonResponse(acart)
    acart = models.ShoppingCart.objects.filter(account=Account)
    return JsonResponse(acart)

def Buy (request):
    Account = request.POST.get('account','Account')
    BookName = request.POST.get('bookname','BookName')
    models.ShoppingCart.objects.create(account=Account,bookname=BookName)
    return HttpResponse(1)

def Delete(request):
    Account = request.POST.get('account','Account')
    BookName = request.POST.get('bookname','BookName')
    models.ShoppingCart.objects.filter(account=Account,bookname=BookName).delete()
    return HttpResponse(1)
