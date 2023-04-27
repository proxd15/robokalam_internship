from django.shortcuts import render
from .models import form

# Create your views here.

def forms(request):
    if request.method == "POST":
        name = request.POST.get('name','')
        number = request.POST.get('number','')
        desc = request.POST.get('desc','')

        Form = form(name = name , number = number , desc = desc)
        Form.save()

    return render(request,'formdb.html')
