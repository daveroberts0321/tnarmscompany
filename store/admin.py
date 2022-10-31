from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Component)
class ComponentAdmin(admin.ModelAdmin):
  '''Admin View for Component'''
  


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
  '''Admin View for Product'''  
  list_filter = ('isactive',) 
  date_hierarchy = 'updated'
  ordering = ('updated','created')


admin.site.register(Category)
class CategoryAdmin(admin.ModelAdmin):
  list_display = ['name', 'slug']
  prepopulated_fields = {'slug':('name')}
  readonly_fields = ('thumbnail_preview',)

  def thumbnail_preview(self, obj):
    return obj.thumbnail_preview

    thumbnail_preview.short_description = 'Thumbnail Preview'
    thumbnail_preview.allow_tags = True