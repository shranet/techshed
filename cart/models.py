from django.db import models

from account.models import User
from main.models import Product
from techshed.validators import PhoneValidator


class Order(models.Model):
    STATUS_NEW = 0
    STATUS_ACCEPTED = 1
    STATUS_REJECTED = 2
    STATUS_IN_DELIVERY = 3
    STATUS_DELIVERED = 4
    STATUS_CLOSED = 5

    PAYMENT_STATUS_NEW = 0
    PAYMENT_STATUS_PREPARE = 1
    PAYMENT_STATUS_COMPLETE = 2
    PAYMENT_STATUS_REJECTED = 3

    user = models.ForeignKey(User, on_delete=models.RESTRICT)
    address = models.TextField()
    phone = models.CharField(max_length=16, validators=[PhoneValidator()])
    zip_code = models.CharField(max_length=20)
    status = models.SmallIntegerField(choices=(
        (STATUS_NEW, "New"),
        (STATUS_ACCEPTED, "Accepted"),
        (STATUS_REJECTED, "Rejected"),
        (STATUS_IN_DELIVERY, "In delivery"),
        (STATUS_DELIVERED, "Delivered"),
        (STATUS_CLOSED, "Closed")
    ))
    payment_status = models.SmallIntegerField(choices=(
        (PAYMENT_STATUS_NEW, "New"),
        (PAYMENT_STATUS_REJECTED, "Rejected"),
        (PAYMENT_STATUS_COMPLETE, "Complete"),
        (PAYMENT_STATUS_PREPARE, "Prepare")
    ), default=PAYMENT_STATUS_NEW)
    order_at = models.DateTimeField(auto_now_add=True)


class OrderProductModel(models.Model):
    order = models.ForeignKey(Order, on_delete=models.RESTRICT)
    product = models.ForeignKey(Product, on_delete=models.RESTRICT)
    amount = models.IntegerField()
