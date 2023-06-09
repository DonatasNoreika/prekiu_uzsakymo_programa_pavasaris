from django.shortcuts import render
from .models import Product, Order
from django.shortcuts import render, get_object_or_404
from django.views import generic

# Create your views here.
def products(request):
    context = {
        "products": Product.objects.all()
    }
    return render(request, "products.html", context=context)


def product(request, product_id):
    context = {
        "product": get_object_or_404(Product, pk=product_id)
    }
    return render(request, 'product.html', context=context)


class OrderListView(generic.ListView):
    model = Order
    template_name = "orders.html"
    context_object_name = 'orders'

class OrderDetailView(generic.DetailView):
    model = Order
    template_name = "order.html"
    context_object_name = 'order'

class MyOrderListView(generic.ListView):
    model = Order
    template_name = "my_orders.html"
    context_object_name = "orders"

    def get_queryset(self):
        return Order.objects.filter(customer=self.request.user)

