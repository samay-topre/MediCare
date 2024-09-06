from django.contrib import admin
from django.urls import path
from authuser import views

urlpatterns = [
    
    path('',views.home,name='home'),
    path('login/',views.LoginPage,name='login'),
    path('signup/',views.SignupPage,name='signup'),
    path('logout/',views.LogoutPage,name='logout'),
    path('index/',views.index,name='index'),
    path('order/',views.order,name='order'),
    path('products/<str:category_name>/', views.products_by_category, name='products_by_category'),
    path('cart/', views.view_cart, name='view_cart'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
        

]
