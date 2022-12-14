from rest_framework import serializers
from .models import Product
from categories.serializers import CategorySerializer


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Product
        fields = ['id', 'product_name', 'price', 'category']
