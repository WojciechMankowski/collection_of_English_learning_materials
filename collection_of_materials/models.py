from django.db import models
from django.db.models import Model, CharField
# Create your models here.

class CollectionOfMaterials(Model):
    title = CharField(max_length=300)
    category = CharField(max_length=300)
    url = CharField(max_length=3000)
    attention = CharField(max_length=3000, null=True, blank=True)

    def __str__(self):
        return f"{self.title} category: {self.category}"
