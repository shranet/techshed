from django.conf import settings as django_settings

from main.models import Category


def settings(request):
    return {
        'settings': django_settings,
    }


def load_categories(request):
    parents = {
        None: []
    }

    for cat in Category.objects.order_by('id').all():
        if cat.parent_id not in parents:
            parents[cat.parent_id] = []

        parents[cat.parent_id].append(cat)

    result = []
    for parent in parents[None]:
        result.append({
            "category": parent,
            "children": parents[parent.id] if parent.id in parents else None
        })

    return {
        'categories': result
    }


def load_cart(request):
    cart = request.session.get('cart')
    return {
        'cart': cart,
        'cart_n': sum(cart.values()) if cart is not None else 0
    }
