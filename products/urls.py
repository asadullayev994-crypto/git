from django.urls import path
from .views import (
    index,
    product_detail,
    like_product,
    save_product,
    add_comment
)

urlpatterns = [
    path('', index, name='index'),
    path('product/<int:id>/', product_detail, name='product_detail'),

    #  LIKE
    path('product/<int:id>/like/', like_product, name='like_product'),

    #  SAVE
    path('product/<int:id>/save/', save_product, name='save_product'),

   # COMMENT
    path('product/<int:id>/comment/', add_comment, name='add_comment'),
]