import uuid

from django.contrib.auth.models import User
from django.db import models
from django.db.models import Model



class Cart(Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

