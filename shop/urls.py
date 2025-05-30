from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("",views.index,name='shop_home'),
    path('about/',views.about,name='aboutUs'),
    path('login/',views.handle_login),
    path('signup/',views.handle_signup),
    path('logout/',views.handle_logout),
    path('profile/',views.profile,name='profile'),
    path('update_profile/',views.update_profile,name='update_profile'),
    path('products/<str:mc>/<str:sc>/<str:br>/',views.products,name='products'),
    path('detail/<int:id>/',views.detail,name='detail'),
    path('add-to-cart/<int:id>/',views.addtoCart),
    path('get-cart/',views.getCart,name='getCart'),
    path('delete-cart/<int:id>',views.deleteCart)
]
