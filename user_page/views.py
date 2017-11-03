from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import Template, Context
from . import models
import json
import random
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib
# Create your views here.
def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

def MyVerVode(request):
    if request.method == 'POST':
        from_addr = 'm17711046053@163.com'
        password = 'a13118905007'
        to_addr = request.POST.get('account','Account')

        user = models.User.objects.all()
        for a_user in user:
            if a_user.account==to_addr:
                return HttpResponse(0)
        PassWord = request.POST.get('password','PassWord')

        smtp_server = 'smtp.163.com'
        i = 0
        while i < 6:
            vercode = random.sample('0123456789', 6)
            i = i + 1
        VerCode = ''.join(vercode)
        msg = MIMEText(VerCode, 'plain', 'utf-8')
        msg['From'] = _format_addr('<%s>' % from_addr)
        msg['To'] = _format_addr('管理员 <%s>' % to_addr)
        msg['Subject'] = Header('验证码', 'utf-8').encode()

        server = smtplib.SMTP(smtp_server, 25)
        server.set_debuglevel(1)
        server.login(from_addr, password)
        server.sendmail(from_addr, [to_addr], msg.as_string())
        server.quit()

        return JsonResponse(VerCode)

def MyRegister(request):
    Account = request.POST.get('account', 'Account')
    PassWord = request.POST.get('password', 'PassWord')
    models.User.objects.create(account=Account,password=PassWord)
    return HttpResponse(1)

def MyLogin(request):
    Account = request.POST.get('account', 'Account')
    PassWord = request.POST.get('password', 'PassWord')
    user=models.User.objects.all()
    for a_user in user:
        if a_user.account==Account and a_user.password==PassWord:
            return render(request,'index/index.html')
        if a_user.account==Account and a_user.password!=PassWord:
            return HttpResponse(1)
    return HttpResponse(0)

def PersonalInformation(request):
    Account = request.POST.get('account','Account')
    a_user = models.User.objects.get(account=Account)
    auser = {}
    auser['account'] = a_user.account
    auser['password'] = a_user.password
    auser['username'] = a_user.username
    return render('request','user_page/personal.html/',auser)

def ModifiPersonal(request):
    Account = request.POST.get('account','Account')
    NewUserName = request.POST.get('newusername','NewUserName')
    NewPassWord = request.POST.get('newpassword','NewPassWord')
    models.User.objects.filter(account=Account).update(username=NewUserName,password=NewPassWord)
    return HttpResponse(1)

