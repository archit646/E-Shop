from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("",views.index,name='shop_home'),
    path('about/',views.about,name='aboutUs'),
    path('contact/',views.contact,name='contactUs'),
    path('tracker/',views.tracker,name='tracking'),
    path('search/',views.search,name='search'),
    path('products/<str:mc>/<str:sc>/<str:br>/',views.products,name='products'),
    path('checkout/',views.checkout,name='checkout')
]
