from django.http import JsonResponse
from django.http import JsonResponse
from django.views import View
from django.views.generic import ListView

from store.models import Product, Order, Customer


class StoreView(ListView):
    template_name = 'store/store.html'
    queryset = Product.objects.all()
    context_object_name = 'products'


class CartView(ListView):
    model = Customer
    template_name = 'store/cart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            customer = self.request.user.customer
            order, created, = Order.objects.get_or_create(customer=customer, complete=False)
            items = order.orderitem_set.all()
        else:
            items, order = [], {'get_cart_items': 0, 'get_cart_total': 0}
        context['items'] = items
        context['order'] = order
        return context


class CheckOutView(ListView):
    template_name = 'store/checkout.html'
    model = Customer

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            customer = self.request.user.customer
            order, created, = Order.objects.get_or_create(customer=customer, complete=False)
            items = order.orderitem_set.all()
        else:
            items, order = [], {'get_cart_items': 0, 'get_cart_total': 0}
        context['items'] = items
        context['order'] = order
        return context


class UpdateItemView(View):
    def get(self, request, *args, **kwargs):
        return JsonResponse('Items as added', safe=False)
