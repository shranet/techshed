from django import template
from django.conf import settings

from techshed.validators import PhoneValidator

register = template.Library()

@register.filter
def phone_format(value):
    return PhoneValidator.format(value)
