from django.contrib import admin
from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name="home"),
    path('cart/',views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('update_item/', views.updateItem, name="update_item"),
    path('login/',views.login_view, name="login"),
    path('logout/',views.logout_view, name="logout"),
    path('register/',views.register, name="register"),
]
