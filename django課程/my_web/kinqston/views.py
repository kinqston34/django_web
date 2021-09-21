from django.db import models
from django.shortcuts import render,redirect
from requests.api import get, post
from .models import Customer,Detail
from .forms import CustomerModelForm,DetailModelForm
# Create your views here.
def base(request):
    return render(request,"base.html")

def index(request):
    customer = Customer.objects.all()
    
    cf = CustomerModelForm()
    
    if request.method == "POST":
        
        cf = CustomerModelForm(request.POST)
        if cf.is_valid :
            cf.save()
        return redirect('./')

    context = {
        'customer': customer,
        'form': cf,
    }
    return render(request,'customer/index.html',context) 

def update(request,pk):
    customer = Customer.objects.get(id=pk)

    cf = CustomerModelForm(instance=customer)

    if request.method == "POST":
        if cf.is_valid :
            cf = CustomerModelForm(request.POST,instance=customer)
            cf.save()
        return redirect('../')

    context = {
        'form': cf,
    }

    return render(request,'customer/update.html',context)


def delete(request,pk):
    customer = Customer.objects.get(id=pk)
    
    if request.method == "POST":
        customer.delete()
        return redirect('../')
    
    context = {
        'customer': customer
    }

    return render(request,'customer/delete.html',context)

def communication(request,pk):
    message = ''
    cus = Customer.objects.get(id=pk)
    try:
        cus_detail = Detail.objects.get(id=pk)
        
        message = '已經建立過囉,請按上面返回鍵'
        context = {
            'message': message
        }
    except:
        df = DetailModelForm()
        if request.method == "POST":
            line_id = request.POST['line_id']
            email = request.POST['email']
            tel = request.POST['tel']
            suggest = request.POST['suggest']
            
            df = Detail.objects.create(id = pk,name = cus,line_id=line_id ,email = email,tel = tel,suggest = suggest)
            df.save()
            message = '新增詳細資料成功'
            return redirect('../')

        context = {
            'customer': cus,
            'form': df, 
            'message': message,
        }
    return render(request,'customer/communication.html',context)
