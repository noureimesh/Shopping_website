import uuid

from django.db import models
from django.db.models import Model


class Product(Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='products', default="![](../products/default.jpg)")
    description = models.CharField(max_length=500)
    price = models.IntegerField()
    quantity = models.IntegerField(default=0)

    def __int__(self):
        pass

    def add(self, name, description, price, quantity):
        self.id = uuid.uuid4()
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    def get_products(self):
        pass