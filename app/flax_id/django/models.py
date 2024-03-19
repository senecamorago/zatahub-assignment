from django.db import models
from .fields import FlaxId


class FlaxMode(models.Model):
    id = FlaxId()

    class Meta:
        abstract = True