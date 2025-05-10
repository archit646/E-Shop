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
    path('products/<str:mc>/<str:sc>/<str:br>/',views.products,name='products'),
    path('detail/<int:id>',views.detail,name='detail')
]
