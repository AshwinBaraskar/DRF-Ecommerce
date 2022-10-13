from django.shortcuts import render
from rest_framework import generics
from .serializers import ProductSerializer
from .models import Product
from django.db.models import Q


class ProductListView(generics.ListAPIView):
    queryset = Product.objects.select_related('category')
    serializer_class = ProductSerializer

    def filter_queryset(self, queryset):
        category = self.request.query_params.get('category')
        price_lt = self.request.query_params.get('price_lt')
        price_gt = self.request.query_params.get('price_gt')
        if category:
            queryset = queryset.filter(category__in=category.split(','))
        if price_gt:
            queryset = queryset.filter(price__gt=price_gt)
        if price_lt:
            queryset = queryset.filter(price__lt=price_lt)
        return queryset

