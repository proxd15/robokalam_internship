from django.http import HttpResponse
from django.shortcuts import render

def web_template(request):
    return render(request , 'index.html')

def form(request):
    return render(request , 'form.html')