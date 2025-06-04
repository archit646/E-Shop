from django.db import models
from django.contrib.auth.models import User
class Category(models.Model):
    # id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=20)
    def __str__(self):
        return self.name
    
class SubCategory(models.Model):
    # id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=20)
    def __str__(self):
       return self.name
    
class Brand(models.Model):
    # id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=20)
    def __str__(self):
        return self.name
    
class Products(models.Model):
    id=models.AutoField(primary_key=True)
    product_name=models.CharField(max_length=50)
    product_desc=models.CharField(max_length=300)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,default='',null=True,blank=True)
    subcategory=models.ForeignKey(SubCategory,on_delete=models.CASCADE,default='',null=True,blank=True)
    brand=models.ForeignKey(Brand,on_delete=models.CASCADE,default='',null=True,blank=True)
    size=models.CharField(max_length=5)
    color=models.CharField(max_length=20,default='')
    base_price=models.IntegerField(default=0)
    discount=models.IntegerField(default=0)
    price=models.IntegerField(default=0)
    stock=models.CharField(max_length=10,default='')
    image1=models.ImageField(upload_to='shop/images',default='')
    image2=models.ImageField(upload_to='shop/images',default='')
    image3=models.ImageField(upload_to='shop/images',default='')
    image4=models.ImageField(upload_to='shop/images',default='')
    pub_date=models.DateField()
    def __str__(self):
        return self.product_name
    
class Buyer(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    email=models.EmailField()
    phone=models.CharField(max_length=12)
    adderessline1=models.CharField(max_length=100)
    adderessline2=models.CharField(max_length=100)
    adderessline3=models.CharField(max_length=100)
    pin=models.IntegerField()
    city=models.CharField(max_length=25)
    state=models.CharField(max_length=40)
    pic=models.ImageField(upload_to='shop/images',default='',null=True,blank=True)
    def __str__(self):
        return self.name
    
class Cart(models.Model):
    id=models.AutoField(primary_key=True)
    product_name=models.CharField(max_length=50)
    price=models.IntegerField(default=0)
    image=models.ImageField(upload_to='shop/images',default='')
    user=models.ForeignKey(User,on_delete=models.CASCADE)