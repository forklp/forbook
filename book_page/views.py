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
    dict1 = {}
    dict2 = {}
    i = 0
    for a_book in abook:
        dict2['account'] = a_book.account
        dict2['contents'] = a_book.contents
        dict1['i'] = dict2
        i = i + 1

    return render(request,'/book_page/comment.html',dict1)


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
    dict1 = {}
    dict2 = {}
    i = 0
    for a_cart in acart:
        dict2['account'] = a_cart.account
        dict2['bookname'] = a_cart.bookname
        dict1['i'] = dict2
        i = i+1
    return render(request,'user_page/cart.html/',dict1)

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
