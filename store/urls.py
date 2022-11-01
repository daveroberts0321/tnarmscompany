from django.urls import path

from . import views

app_name = 'store'

urlpatterns = [
    ##Cart##
    #path('cart/', CartView.as_view(), name='cart'),
    path('summary/', views.cart_summary, name='cartsummary'),
]