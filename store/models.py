from django.db import models

# Create your models here.
class Category(models.Model):
  """Model definition for Category."""
  name = models.CharField("Category Name", max_length=50, db_index = True)
  slug = models.SlugField(unique= True)


  # TODO: Define fields here

  class Meta:
    """Meta definition for Category."""

    verbose_name = 'Category'
    verbose_name_plural = 'Categories'



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

  def save(self):
    """Save method for Component."""
    pass


  # TODO: Define custom methods here


class Product(models.Model):
  """Model definition for Product."""

  # TODO: Define fields here

  name = models.CharField("Product Name", max_length=50)
  category= models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE)
  components= models.ManyToManyField(Component)
  shortdesc = models.CharField("Short Desc", max_length=50)
  longdesc = models.TextField("Long Desc")
  price = models.DecimalField("Product Base Price", max_digits=5, decimal_places=2)
  mainimg = models.ImageField("Main Image", upload_to='images/', height_field=None, width_field=None, max_length=None)
  created = models.DateField("Date Created", auto_now=False, auto_now_add=True)
  updated = models.DateField("Date Updated", auto_now=True, auto_now_add=False)
  isactive = models.BooleanField(default=True)


  class Meta:
    """Meta definition for Product."""

    verbose_name = 'Product'
    verbose_name_plural = 'Products'
    ordering = ['-updated']# orders by last item updated 

  def __str__(self):
    """Unicode representation of Product."""
    pass

  def save(self):
    """Save method for Product."""
    pass

  def get_absolute_url(self):
    """Return absolute url for Product."""
    return ('')

  # TODO: Define custom methods here

