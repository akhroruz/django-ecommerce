from django.contrib import admin
from django.urls import path

from store.views import StoreView, CartView, CheckOutView, UpdateItemView

urlpatterns = [
    path('', StoreView.as_view(), name='store'),
    path('cart', CartView.as_view(), name='cart'),
    path('checkout', CheckOutView.as_view(), name='checkout'),
    path('update-item', UpdateItemView.as_view(), name='update_item')
]
