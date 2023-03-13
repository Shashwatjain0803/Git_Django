from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def hello(request):
    return HttpResponse('Welcome to Django my friend!')



def first_html(request):
    return render(request,'first_html.html')

def forms_html(request):
    return render(request,'forms.html')