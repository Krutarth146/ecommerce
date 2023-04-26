from django.urls import path,include
from .views import *

urlpatterns = [
    path('createproduct/',CreateProduct.as_view(),name='createproduct'),
    path('listproducts/',ListProducts.as_view(),name='listproducts'),
    path('detailproduct/<int:pk>',DetailProduct.as_view(),name='detailproduct'),
    path('updateproduct/<int:pk>',UpdateProduct.as_view(),name='updateproduct'),
    path('deleteproduct/<int:pk>',DeleteProduct.as_view(),name='deleteproduct'),

    # ---------------------------------------
    path('createcategory/',CreateCategory.as_view(),name='createcategory'),
    path('listcategories/',ListCategory.as_view(),name='listcategories'),
    path('deletecategory/<int:pk>',DeleteCategory.as_view(),name='deletecategory'),
    path('updatecategory/<int:pk>',UpdateCategory.as_view(),name='updatecategory'),
    path('',Index.as_view(),name='index'),
    path('cart/',Cart.as_view(),name='cart'),
    path('checkout/',CheckOut.as_view(),name='checkout'),
]
