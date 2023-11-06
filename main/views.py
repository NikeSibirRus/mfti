

from django.http import HttpResponse
from django.shortcuts import render
from django import forms

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)


def index(request):
    return render(request,'main/index.html')

def about(request):
    return render(request, 'main/about.html', { "form" : NameForm() })

def contacts(request):
    return render(request, 'main/contacts.html')

def content(request):
    return render(request, 'main/content.html')

#def content(request): return  HttpResponse('<h1>контакты</h1>')
