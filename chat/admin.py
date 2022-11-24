from django.contrib import admin
from django_otp.admin import OTPAdminSite

from .models import UserProfile, Messages, Friends

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Messages)
admin.site.register(Friends)
# admin.site.__class__ = OTPAdminSite
