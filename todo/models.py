from django.db import models


class ShoppingItem(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    description = models.TextField(blank=True, null=True)
    quantity = models.IntegerField(default=1)
    is_completed = models.BooleanField(default=False)

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name', 'description', 'quantity', 'is_completed', 'created_on', 'updated_on')

    def __str__(self):
        return self.name

