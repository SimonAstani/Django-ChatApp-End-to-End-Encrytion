import random

from django import template
from django.conf import settings

from chat.views import decrypt

register = template.Library()


@register.filter
def decrypt_text(text):
    plain_text = decrypt(text)
    print(plain_text)
    return plain_text

