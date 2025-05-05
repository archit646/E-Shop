from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def index(request):
    products=Products.objects.all()
    params={'products':products}
    return render(request,'shop/index.html',params)

def about(request):
    return render(request,'shop/about.html')

def contact(request):
    return render(request,'shop/contact.html')

def tracker(request):
    return HttpResponse("We are in tracker")

def search(request):
    return HttpResponse("We are in search")

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

def checkout(request):
    return HttpResponse("We are in checkout")