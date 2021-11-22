from django.conf import settings as django_settings

from main.models import Category


def settings(request):
    return {
        'settings': django_settings,
    }


def load_categories(request):
    return {
        'categories': Category.objects.order_by('id').all()
    }
