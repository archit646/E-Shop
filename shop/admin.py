from django.contrib import admin
from .models import *

admin.site.register((Category,SubCategory,Brand,Products,Buyer))

