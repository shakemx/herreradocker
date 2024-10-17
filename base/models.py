from uuid import uuid4

from django.db import models


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField('Activo', default=True)
    
    class Meta:
        abstract = True
