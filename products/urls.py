from django.urls import path
from .views import (
    index,
    product_detail,
    like_product,
    save_product,
    add_comment,
    create_order
)

urlpatterns = [
    path('', index, name='index'),
    path('product/<int:id>/', product_detail, name='product_detail'),


    path('product/<int:id>/like/', like_product, name='like_product'),


    path('product/<int:id>/save/', save_product, name='save_product'),

 
    path('product/<int:id>/comment/', add_comment, name='add_comment'),
     
   path('order/<int:pk>/', create_order, name='order'),
]