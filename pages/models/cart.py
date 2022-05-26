import uuid

from django.db import models
from django.db.models import Model

from .user import User


class Cart(Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __init__(self, user_id):
        self.id = uuid.uuid4()
        self.user_id = user_id
        self.cart_products = []
