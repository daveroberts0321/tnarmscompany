from django.views.generic import TemplateView, ListView, DetailView
from store.models import Product, Category

#staticpages Views 
class HomePageView(ListView):# listings by category
    model = Category
    template_name = "pages/home.html"


#products filtered by category and put on their own page 
class AboutPageView(TemplateView):
    template_name = "pages/about.html"

class TnArms15View(ListView):#successfully connected
    model = Product  
    queryset = Product.objects.filter(category__name__contains="ar15").all()
    context_object_name = 'context'
    template_name = "pages/categorylist.html"  

class Ar308View(ListView):
    model = Product  
    queryset = Product.objects.filter(category__name__contains="ar308").all()
    context_object_name = 'context'
    template_name = "pages/categorylist.html"

class Tac9View(ListView):
    model = Product  
    queryset = Product.objects.filter(category__name__contains="tac9").all()
    context_object_name = 'context'
    template_name = "pages/categorylist.html"

class PartsView(ListView):
    model = Product  
    queryset = Product.objects.filter(category__name__contains="parts").all()
    context_object_name = 'context'
    template_name = "pages/categorylist.html"

class Tn9pView(ListView):
    model = Product  
    queryset = Product.objects.filter(category__name__contains="tn9p").all()
    context_object_name = 'context'
    template_name = "pages/categorylist.html"

# Product Detail 
class ProductView(DetailView):
    model = Product
    template_name = 'pages/productdetail.html'
    context_object_name = 'object'





