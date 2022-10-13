from django.shortcuts import render
from rest_framework import generics
from django.db.models import Prefetch
from .models import Category
from products.models import Product
from .serializers import CategorySerializer, CategoryProductSerializer


class GetCategoryIdView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'id'


class GetCategoryNameView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_queryset(self):
        name = self.request.query_params.get('name')
        if name:
            return self.queryset.filter(name=name)
        return self.queryset.all()


class FeaturedCategoryListView(generics.ListAPIView):
    serializer_class = CategoryProductSerializer

    def get_queryset(self):
        queryset = Category.objects.filter(is_featured=True) \
            .prefetch_related(
                Prefetch(
                    "product_set", Product.objects.all(), to_attr="products"
                )
            )
        return queryset
