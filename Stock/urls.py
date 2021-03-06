"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.decorators import login_required
from . import views

app_name = 'stock'

urlpatterns = [
    path('inventory', login_required(views.InventoryHome.as_view()) , name='inventory'),
    path('inventory-add', login_required(views.Inventory_Add.as_view()) , name='inventory-add'),

    path('inventory/delete', login_required(views.InventoryDelete) , name='inventory-delete'),


    path('products', login_required(views.ProductHome.as_view()) , name='product'),
    path('products-add', login_required(views.Product_Add.as_view()) , name='product-add'),

    path('products/delete', login_required(views.product_delete) , name='product-delete'),
]
