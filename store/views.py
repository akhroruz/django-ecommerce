from django.views.generic import TemplateView, ListView

from store.models import Product, Order


class StoreView(ListView):
    template_name = 'store/store.html'
    queryset = Product.objects.all()
    context_object_name = 'products'


class CartView(ListView):
    template_name = 'store/cart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            customer = self.request.user.customer
            order, created, = Order.objects.get_or_create(customer=customer, complete=False)
            items = order.orderitem_set.all()
        else:
            items = []

        context['items'] = items
        return context


class CheckOutView(TemplateView):
    template_name = 'store/checkout.html'
