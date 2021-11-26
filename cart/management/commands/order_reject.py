import datetime

from django.core.management.base import BaseCommand
from django.db import transaction
from django.db.models import F

from cart.models import Order, OrderProduct
from main.models import Product


class Command(BaseCommand):
    def handle(self, *args, **options):
        with transaction.atomic():
            for row in Order.objects.filter(status=Order.STATUS_NEW,
                                            order_at__lte=datetime.datetime.now() - datetime.timedelta(minutes=10)
                                            ).select_for_update().all():
                row.status = Order.STATUS_REJECTED
                row.save()

                for p in OrderProduct.objects.filter(order=row).all():
                    Product.objects.filter(id=p.product_id).update(available=F("available") + p.amount)
