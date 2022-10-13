from . import views
from django.urls import path

urlpatterns = [
    path('products', views.ProductListView.as_view(), name='get-particular-product')
]