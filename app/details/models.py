from typing import Self
from django.db import models

# Create your models here.
class Draws(models.Model):
    name = models.CharField(max_length=13)
    comment = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name