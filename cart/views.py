from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction
from django.db.models import F
from django.shortcuts import render, redirect
from django.views.generic import ListView

from cart.form import OrderForm
from cart.models import OrderProduct, Order
from main.models import Product


def cart_change(request, pid, action):
    product = Product.objects.get(id=pid)
    pid = str(product.id)
    cart = request.session.get('cart', {})
    if cart is None:
        cart = {}

    if action == 'inc':
        cart[pid] = min(cart.get(pid, 0) + 1, product.available)
    elif action == 'dec':
        cart[pid] = max(cart.get(pid, 0) - 1, 0)

    if cart[pid] == 0:
        del cart[pid]

    request.session['cart'] = cart

    return redirect('main:product', product.id)


def cart_list(request):
    cart = request.session.get('cart', {})
    if not cart:
        return redirect('main:index')

    products = Product.objects.filter(id__in=cart.keys()).all()
    result = [{
        'p': row,
        'n': cart[str(row.id)],
        'total': cart[str(row.id)] * row.price
    } for row in products]

    return render(request, 'cart/product.html', {
        'list': result,
        'total': sum([row['total'] for row in result])
    })


@login_required
def cart_checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        return redirect('main:index')

    products = Product.objects.filter(id__in=cart.keys()).all()
    result = [{
        'p': row,
        'n': cart[str(row.id)],
        'total': cart[str(row.id)] * row.price
    } for row in products]

    form = OrderForm()
    if request.method == 'POST':
        form = OrderForm(data=request.POST)
        if form.is_valid():
            # transaction
            with transaction.atomic():
                form.instance.order_total_price = sum([row['total'] for row in result])
                form.instance.status = Order.STATUS_NEW
                form.instance.user = request.user
                order = form.save()

                products = []
                for pid, n in cart.items():
                    k = Product.objects.filter(id=pid, available__gte=n).update(available=F("available") - n)
                    if not k:
                        raise Exception(f"Mahsulot yetarlicha mavjud emas. {pid}={n}")
                    products.append(OrderProduct(order=order, product_id=pid, amount=n))

                OrderProduct.objects.bulk_create(products)

                request.session['cart'] = {}

                return redirect('main:index')

    return render(request, 'cart/checkout.html', {
        'form': form,
        'products': result
    })


class OrderListView(LoginRequiredMixin, ListView):
    model = Order
    template_name = 'cart/orders.html'

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)


def order_pay(request, oid):
    Order.objects.filter(id=oid, status=Order.STATUS_NEW).update(status=Order.STATUS_ACCEPTED,
                                                                 payment_status=Order.PAYMENT_STATUS_COMPLETE)

    return redirect("cart:orders")

