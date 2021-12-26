from django.shortcuts import redirect, render
from .models import Product, Inventory
from django.views.generic import ListView, CreateView
from .forms import Product_Add, Inventory_Add

# Create your views here.

class InventoryHome(ListView):
    model = Inventory
    template_name = 'inventory.html'


class ProductHome(ListView):
    model = Product
    template_name = 'product.html'


class Inventory_Add(CreateView):
    models = Inventory
    form_class = Inventory_Add
    template_name = 'inventory-add.html'
    success_url = '/stock/inventory'


def InventoryDelete(request):
    id = request.POST['product']
    obj = Inventory.objects.get(id=id)
    obj.delete()
    return redirect(to='stock:inventory')


class Product_Add(CreateView):
    models = Product
    form_class = Product_Add
    template_name = 'product-add.html'
    success_url = '/stock/products'


def product_delete(request):
    id = request.POST['product']
    obj = Product.objects.get(id=id)
    obj.delete()
    return redirect(to='stock:product')