from django.shortcuts import render
from .models import Category, Component, Product 


# Context preprocessor views here.
# category and product 
def categories(request):
  return{
    'category':Category.objects.all(),
    'product':Product.objects.all(),
  }
