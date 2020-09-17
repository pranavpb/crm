from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import *
 
def home(request):
    return render(request,'pageone.html')
"""def home_1(request):
    return render(request,'pagetwo.html')"""

def home_2(request,id=0):
    if(request.method=="GET"):
        if(id==0):
            form = supplier_form()
        else:
            id_value = supplier.objects.get(id=id)
            form = supplier_form(instance = id_value)
        return render(request,'pagetwo.html',{"form":form,})
    else:
        if(id==0):
            form=supplier_form(request.POST)
        else:
            id_value=supplier.objects.get(id=id)
            form = supplier_form(request.POST,instance = id_value)
        if(form.is_valid()==True):
            form.save()
        all_data=supplier.objects.all()
        return render(request,'pagetwo.html',{"form":form,"all":all_data})