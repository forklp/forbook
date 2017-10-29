from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def demo1(request):
    return render(request, 'demos/demo1.html')
