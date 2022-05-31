import uuid

from django.db import models
from django.db.models import Model

from .cart import Cart
from .product import Product


class CartProduct(Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart_id = models.ForeignKey(Cart, on_delete=models.CASCADE)
