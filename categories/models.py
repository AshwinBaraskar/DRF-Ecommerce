from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

# /categories/featured
#
# [
#     {
#         id
#         name
#         products: [
#             {
#                 id
#                 product_name
#                 price
#             }
#         ]
#     }
# ]

