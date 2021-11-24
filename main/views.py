from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django_filters.views import FilterView

from main.filters import ProductFilter
from main.models import TopCategory, Product


class MainIndexView(TemplateView):
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        top = [row for row in TopCategory.objects.filter(status=TopCategory.STATUS_ACTIVE).order_by('?').all()[:2]]
        if len(top) == 1:
            top.append(top[0])

        context['top_categories'] = top
        context['top_sold'] = Product.objects.filter(status=Product.STATUS_APPROVED).order_by('-sold')[:6]

        return context


class MainAboutView(TemplateView):
    template_name = 'main/about.html'


class MainContactView(TemplateView):
    template_name = 'main/contact.html'


class MainCategoryView(FilterView):
    queryset = Product.objects.filter(status=Product.STATUS_APPROVED).all()
    discount = False
    template_name = 'main/products.html'
    filterset_class = ProductFilter

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.discount:
            queryset = queryset.filter(has_discount=True)

        cat_id = self.kwargs.get('cat_id')
        if cat_id is not None:
            queryset = queryset.filter(category_id=cat_id)

        return queryset


class ProductView(DetailView):
    model = Product
    template_name = 'main/product.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        cart = self.request.session.get('cart')
        pid = str(self.object.id)
        context['cart_p'] = cart[pid] if cart and pid in cart else 0
        return context

