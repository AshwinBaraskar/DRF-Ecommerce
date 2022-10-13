from rest_framework import serializers
from .models import Category
from products.models import Product


class ProductInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            "id",
            "product_name",
            "price"
        ]


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class CategoryProductSerializer(serializers.ModelSerializer):
    products = ProductInfoSerializer(many=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'products']

