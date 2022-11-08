from django.urls import path

from .views import *

app_name= 'pages'

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("about/", AboutPageView.as_view(), name="about"),
    path('tnarms15/', TnArms15View.as_view(), name='tnarms15'),
    path('ar308/', Ar308View.as_view(), name='ar308'),
    path('tac9/', Tac9View.as_view(), name='tac9'),
    path('tn9p/', Tn9pView.as_view(), name='tn9p'),
    path('parts/', PartsView.as_view(), name='parts'),
    path('80s/', BlankView.as_view(), name='80s'),
    #product detail page
    path('product/<int:pk>',ProductView.as_view(), name='productdetail'),
    ##Cart##
    #path('cart/', CartView.as_view(), name='cart'),
]
