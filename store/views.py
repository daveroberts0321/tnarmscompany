from django.shortcuts import render

from .models import Category, Component, Product


# Context preprocessor views here. Can see in settings.py
# category and product 
def categories(request):
  return{
    'category':Category.objects.all(),
    'product':Product.objects.all(),
  }

#cart 
def cart_summary(request):
  return render(request, 'store/cart/summary.html')