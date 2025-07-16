from django.db import models
from kitchen.models import Kitchen

class Brand(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    kitchen = models.ForeignKey(Kitchen, on_delete=models.CASCADE, related_name='brands')

    def __str__(self):
        return self.name