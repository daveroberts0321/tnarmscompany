from django.urls import path

from . import views

app_name = 'store'

urlpatterns = [
    ##Cart##
    path('summary/', views.cart_summary, name='cartsummary'),
]