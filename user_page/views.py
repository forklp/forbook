from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
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
        #models.User.objects.create(account=to_addr, password=PassWord)
        return HttpResponse(1)



def MyLogin(request):
    Account = request.POST.get('account', 'Account')
    PassWord = request.POST.get('password', 'PassWord')
    user=models.User.objects.all()
    for a_user in user:
        if a_user.account==Account and a_user.password==PassWord:
            response = HttpResponse(2)
            response.set_cookie('Account',Account,30)
            return response
        if a_user.account==Account and a_user.password!=PassWord:
            return HttpResponse(1)
    return HttpResponse(0)


def ModifiAccount(request):
    OldAccount = request.POST.get('oldusername', 'OldAccount')
    NewAccount = request.POST.get('newusername','NewAccount')
    models.User.objects.filter(account=OldAccount).update(account=NewAccount)

def ModifiPassword(request):
    OldPassWord = request.POST.get('oldpasswd', 'OldPassWord')
    NewPassWord = request.POST.get('newpasswd', 'NewPassWord')
    models.User.objects.filter(password=OldPassWord).update(password=NewPassWord)
