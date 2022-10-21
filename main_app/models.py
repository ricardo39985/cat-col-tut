from unicodedata import name
from django.db import models
from django.utils import timezone

# Create your models here.


class Cat(models.Model):
    name = models.CharField(max_length=200)
    breed = models.TextField(null=True, blank=True)
    age= models.IntegerField()
    # participants =
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
