from django.urls import path
from .views import *

urlpatterns = [

    path('', home, name='home'),

    path('deleteProduct/', deleteProduct, name='deleteProduct'),

    path('updateProduct/', updateProduct, name='updateProduct'),

    path('saveuser/', saveuser, name='saveuser'),

    path('Productlist/', Productlist, name='Productlist'),

    path('newProductForm/', newProductForm, name='newProductForm'),

    path('updateProductForm/', updateProductForm, name='updateProductForm'),

]