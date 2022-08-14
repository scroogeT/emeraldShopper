from django.db import models


class ShoppingItem(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    quantity = models.IntegerField(default=1)

    class Meta:
        ordering = ('name',)

