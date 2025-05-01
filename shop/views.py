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
    
    products=Products.objects.all()
    params={'maincategory':maincategory,'subcategory':subcategory,'brand':brand,'products':products}
    return render(request,'shop/products.html',params)

def checkout(request):
    return HttpResponse("We are in checkout")