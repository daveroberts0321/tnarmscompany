from django.db import models
from django.urls import reverse
from django.utils.html import mark_safe
from django_resized import ResizedImageField
from django.conf import settings

from django.contrib.auth import get_user_model

from model_utils.fields import StatusField
from model_utils import Choices #https://django-model-utils.readthedocs.io/en/latest/fields.html

#Review for addeed model functionality https://django-model-utils.readthedocs.io/en/latest/fields.html

# User reference 


# Create your models here.
class Category(models.Model):
  """Model definition for Category."""
  CATEGORY = Choices('ar15', 'ar308', 'tac9','tn9p','80%','parts')
  
  
  name = StatusField(choices_name='CATEGORY', max_length=50, db_index = True)
  slug = models.SlugField(unique= True)
  mainimg = ResizedImageField(size=[800, 600], upload_to='static/images/', default='static/images/default.jpg')
  subtext = models.TextField(null=True, blank=True)
  desc = models.TextField(null=True, blank=True)

  # TODO: Define fields here

  class Meta:
    """Meta definition for Category."""
    ordering = ["name"]
    verbose_name = 'Category'
    verbose_name_plural = 'Categories'
    

  @property
  def thumbnail_preview(self):
    if self.thumbnail:
        _thumbnail = get_thumbnail(self.thumbnail,
                                '300x300',
                                upscale=False,
                                crop=False,
                                quality=100)
        return format_html('<img src="{}" width="{}" height="{}">'.format(_thumbnail.url, _thumbnail.width, _thumbnail.height))
    return ""


  def get_absolute_url(self):
        return reverse("category", kwargs={"pk": self.pk})


  def __str__(self):
    """Unicode representation of Category."""
    return f'Category: {self.name}, slug:{self.slug}'

class Component(models.Model):
  """Model definition for Component."""
  name = models.CharField("Component Name", max_length=50)
  amount = models.IntegerField(default=0)
  color = models.CharField("Component Color", max_length=50)


  # TODO: Define fields here

  class Meta:
    """Meta definition for Component."""

    verbose_name = 'Component'
    verbose_name_plural = 'Components'

  def __str__(self):
    """Unicode representation of Component."""
    return f'Component: {self.name}, Color: {self.color}, Inventory: {self.amount}'

  # TODO: Define custom methods here

#product manager to only return isactive products 
class ProductManager(models.Manager):
  def get_queryset(self):
        return super().get_queryset().filter(isactive=True)


class Product(models.Model):
  """Model definition for Product."""

  # TODO: Define fields here

  name = models.CharField("Product Name", max_length=50)
  category= models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE)
  components= models.ManyToManyField(Component)
  shortdesc = models.CharField("Short Desc", max_length=50)
  longdesc = models.TextField("Long Desc")
  price = models.DecimalField("Product Base Price", max_digits=5, decimal_places=2)
  mainimg = ResizedImageField(size=[800, 600], upload_to='static/images/', default='static/images/default.jpg')
  created = models.DateField("Date Created", auto_now=False, auto_now_add=True)
  updated = models.DateField("Date Updated", auto_now=True, auto_now_add=False)
  isactive = models.BooleanField(default=True)
  isfeatured = models.BooleanField(default=True)
  #modelManager to only return isactive products
  objects=models.Manager()
  activeproducts= ProductManager()


  @property
  def thumbnail_preview(self):
    if self.thumbnail:
        _thumbnail = get_thumbnail(self.thumbnail,
                                '300x300',
                                upscale=False,
                                crop=False,
                                quality=100)
        return format_html('<img src="{}" width="{}" height="{}">'.format(_thumbnail.url, _thumbnail.width, _thumbnail.height))
    return ""

  class Meta:
    """Meta definition for Product."""

    verbose_name = 'Product'
    verbose_name_plural = 'Products'
    ordering = ['-updated']# orders by last item updated 

  def __str__(self):
    """Unicode representation of Product."""
    return f'Product: {self.name}, Price: {self.price}, Components: {self.components.name},'


  def get_absolute_url(self):
    """Return absolute url for Product."""
    return reverse('pages:productdetail', args=[str(self.id)])

  # TODO: Define custom methods here

################CART Models with Unicorn Functionality ##########################

class CartItem(models.Model):
  """Products added to the Cart ( Django Unicorn Component)."""

  product = models.ForeignKey(Product,null=True, on_delete=models.SET_NULL)
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
  quantity = models.PositiveIntegerField(default=1)
  added = models.DateTimeField("Date/Time Added", auto_now=False, auto_now_add=False)
  
  
  # TODO: Unicorn Functionality

  

  class Meta:
    """Meta definition for CartItem."""

    verbose_name = 'CartItem'
    verbose_name_plural = 'CartItems'

  def __str__(self):
    """Unicode representation of CartItem."""
    return f'Customer: {self.user.email}, Product: {self.product.name}'

