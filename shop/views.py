from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import *

def index(request):
    products=Products.objects.all()
    params={'products':products}
    print(request.user)
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
           return render(request,'shop/login.html')
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
    # return render(request,'shop/login.html')
    return redirect('/shop/login')

def profile(request):
    if request.user.is_superuser:
        return redirect('/shop/admin')
    else:
        try:
           data=Buyer.objects.get(user=request.user)
        #    print(data.pic.url)
        except Buyer.DoesNotExist:
            return redirect('/shop/update_profile')
    return render(request,'shop/profile.html',{'data':data})

def update_profile(request):
    try:
        data=Buyer.objects.get(user=request.user) 
    except Buyer.DoesNotExist:
        data=None
    if request.method=="POST":        
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        adderess1=request.POST.get('adderess1')
        adderess2=request.POST.get('adderess2')
        adderess3=request.POST.get('adderess3')
        pin=request.POST.get('pin')
        city=request.POST.get('city')
        state=request.POST.get('state')
        pic=request.FILES.get('pic')
        if data:
            data.name=name
            data.email=email
            data.phone=phone
            data.adderessline1=adderess1
            data.adderessline2=adderess2
            data.adderessline3=adderess3
            data.pin=pin
            data.city=city
            data.state=state
            data.pic=pic
            data.save()
            
        else:
            buyer=Buyer(name=name,user=request.user,email=email,phone=phone,adderessline1=adderess1,adderessline2=adderess2,adderessline3=adderess3,pin=pin,city=city,state=state,pic=pic)
            buyer.save()
            messages.success(request,'Profile Updated Successfully')
            return redirect('/shop/profile')
    return render(request,'shop/update_profile.html',{'data':data})

    
    

    