from typing import List
from django.db import models
from django.shortcuts import render
from .models import Expense
from django.views.generic import ListView, CreateView
from django.shortcuts import redirect
from django.contrib import messages
from .forms import expense_add

# Create your views here.

class Home(ListView):
    model = Expense
    template_name = 'expense.html'


class Add(CreateView):
    models = Expense
    form_class = expense_add
    template_name = 'expense-add.html'
    success_url = '/expense/home'


def delete(request):
    id = request.POST['product']
    obj = Expense.objects.get(id=id)
    obj.delete()
    messages.error(request, 'Your actions have been succesfully saved !')
    return redirect(to='expense:home')