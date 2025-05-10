from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import *

def index(request):
    products=Products.objects.all()
    params={'products':products}
    return render(request,'shop/index.html',params)

def about(request):
    return render(request,'shop/about.html')



def products(request,mc,sc,br):
    maincategory=Category.objects.all()
    subcategory=SubCategory.objects.all()
    brand=Brand.objects.all()
    if mc=='All' and sc=='All' and br=='All':
         products=Products.objects.all().order_by('-id')
    elif mc!='All' and sc=='All' and br=='All':
        products=Products.objects.filter(category=Category.objects.get(name=mc)).order_by('-id')
    elif mc!='All' and sc!='All' and br=='All':
         products=Products.objects.filter(category=Category.objects.get(name=mc),subcategory=SubCategory.objects.get(name=sc)).order_by('-id')
    elif mc!='All' and sc!='All' and br!='All':
        products=Products.objects.filter(category=Category.objects.get(name=mc),subcategory=SubCategory.objects.get(name=sc),brand=Brand.objects.get(name=br)).order_by('-id')
    elif mc=='All' and sc!='All' and br=='All':
        products=Products.objects.filter(subcategory=SubCategory.objects.get(name=sc)).order_by('-id')
    elif mc=='All' and sc=='All' and br!='All':
        products=Products.objects.filter(brand=Brand.objects.get(name=br)).order_by('-id')
    elif mc!='All' and sc=='All' and br=='All':
        products=Products.objects.filter(category=Category.objects.get(name=mc)).order_by('-id')
    elif mc=='All' and sc!='All' and br!='All':
        products=Products.objects.filter(subcategory=SubCategory.objects.get(name=sc),brand=Brand.objects.get(name=br)).order_by('-id')
    elif mc!='All' and sc=='All' and br!='All':
        products=Products.objects.filter(category=Category.objects.get(name=mc),brand=Brand.objects.get(name=br)).order_by('-id')
        
    params={'maincategory':maincategory,'subcategory':subcategory,'brand':brand,'products':products,'mc':mc,'sc':sc,'br':br}
    return render(request,'shop/products.html',params)

def detail(request,id):
    data=Products.objects.get(id=id)
    params={'data':data}
    return render(request,'shop/detail.html',params)

def handle_login(request):
    if request.method=='POST':
        
        loginusername=request.POST.get('username')
        loginpassword=request.POST.get('password')
        user=authenticate(username=loginusername,password=loginpassword)
        if user is not None:
           login(request,user)
           messages.success(request,'Logged in Successfully')
           return redirect('/shop/')
        else:
           messages.error(request,'Invalid Username or Password')  
           return render('shop/index.html')
    return render(request,'shop/login.html')

def handle_signup(request):
    if request.method=='POST':
        try:
          username=request.POST.get('username')
          fname=request.POST.get('fname')
          lname=request.POST.get('lname')
          email=request.POST.get('email')
          password=request.POST.get('password')
          rpassword=request.POST.get('repeat-password')
          if password!=rpassword:
              messages.error(request,'Password Are Not Same')
              return redirect('/shop/signup/')
          else:
              myuser=User.objects.create_user(username,email,password)
              myuser.first_name=fname
              myuser.last_name=lname
              myuser.save()
              messages.success(request,'Registered Successfully')
              return render('/shop/login/')
        except:
            messages.error(request,'Internal Error')  
            return redirect('/shop/signup/')    
    return render(request,'shop/signup.html')

def handle_logout(request):
    logout(request)
    messages.success(request,'Logout Successfully')
    return render(request,'shop/login.html')

    
    

    