from django_unicorn.components import UnicornView, QuerySetType
from django.contrib.auth.models import User
from store.models import CartItem
from django.db.models import F

from django.conf import settings
from django.contrib.auth import get_user_model

# to get a cookie from django...   device=request.COOKIES['device']

settings.AUTH_USER_MODEL
class CartView(UnicornView):
    user_products: QuerySetType(CartItem)= None 
    user_pk: str = ""
    device = getCookie('device')

    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs) # calling super is required
        self.user_pk = kwargs.get('user')#self.user_pk = kwargs.get('user')
        self.user_products = CartItem.objects.filter(user=self.user_pk)


    def add_item(self, product_pk):
        item, created = CartItem.objects.get_or_create(user_id=self.user_pk,
         product_id=product_pk)

        if not created:
            item.quantity = F('quantity') + 1
            item.save()
        self.user_products = CartItem.objects.filter(user=self.user_pk)