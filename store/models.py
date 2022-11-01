from django.db import models
from django.urls import reverse
from django_resized import ResizedImageField
from django.utils.html import mark_safe

CATEGORY = [
  ('ar15','ar15'),
  ('ar308','ar308'),
  ('tac9','tac9'),
  ('tn9p','tn9p'),
  ('80%','80%'),
  ('parts','parts'),
]

# Create your models here.
class Category(models.Model):
  """Model definition for Category."""
  name = models.CharField("Category Name",choices=CATEGORY, max_length=50, db_index = True)
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

