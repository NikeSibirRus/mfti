

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request,'main/index.html')

def about(request):
    return render(request, 'main/about.html')

def contacts(request):
    return render(request, 'main/contacts.html')

def content(request):
    return render(request, 'main/content.html')

#def content(request): return  HttpResponse('<h1>контакты</h1>')