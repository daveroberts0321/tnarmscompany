from django.urls import path

from . import views

app_name = 'store'

urlpatterns = [
    ##Cart##
    path('cart/', views.cart_summary, name='cart'),
]