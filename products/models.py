from django.db import models
from categories.models import Category


class Product(models.Model):
    product_name = models.CharField(max_length=100, unique=True)
    price = models.DecimalField(decimal_places=2, max_digits=15)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'product'
        unique_together = ['product_name', 'category']

    def __str__(self):
        return f"{self.product_name} - {self.price}"