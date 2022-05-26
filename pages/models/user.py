import uuid

from django.db import models
from django.db.models import Model



class User(Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    passwort = models.CharField(max_length=20)

    def __init__(self, first_name, last_name, email, passwort):
        self.id = uuid.uuid4()
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.passwort = passwort
        from .cart import Cart
        self.cart = Cart(self.id)
