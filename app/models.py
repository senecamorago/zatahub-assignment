from django.db import models
from app.flax_id.django.fields import FlaxId


class Meeting(models.Model):
    id = FlaxId(primary_key=True)
    name = models.CharField(max_length=512)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def _str_(self):
        return self.id


class Note(models.Model):
    id = FlaxId(primary_key=True)
    meeting = models.ForeignKey(Meeting, on_delete=models.CASCADE)
    content = models.CharField(max_length=1024, blank=True)
    publish_transaction_id = models.CharField(max_length=512)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def _str_(self):
        return self.id
