
from ..models import Product



class ProductRepo:

    def __int__(self):
        pass

    def get_products(self):
        return Product.objects.order_by('-name')
