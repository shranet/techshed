from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from cart.form import OrderForm
from main.models import Product


def cart_change(request, pid, action):
    product = Product.objects.get(id=pid)
    pid = str(product.id)
    cart = request.session.get('cart', {})

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
            pass

    return render(request, 'cart/checkout.html', {
        'form': form,
        'products': result
    })
