from django.urls import path
from . import views

urlpatterns = [
    path('categories/<int:id>/', views.GetCategoryIdView.as_view(), name='category-view'),
    path('categories', views.GetCategoryNameView.as_view(), name='get-name'),
    path('categories/featured/', views.FeaturedCategoryListView.as_view(), name='featured-view')

]
