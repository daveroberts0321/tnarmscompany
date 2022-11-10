from django_unicorn.components import UnicornView, QuerySetType
from django.contrib.auth.models import User
from store.models import CartItem

class CartView(UnicornView):
    user_products: QuerySetType(CartItem)= None 
    user_pk: str

    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs) # calling super is required
        self.user_pk = kwargs.get('user')
        self.user_products = CartItem.objects.filter(user=self.user_pk)