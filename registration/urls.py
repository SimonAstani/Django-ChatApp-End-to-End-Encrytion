from django.contrib.auth.views import LoginView
from django.urls import path
from django_otp.forms import OTPAuthenticationForm

from registration.views import RegisterView

urlpatterns = [
    # path('signup/', RegisterView.as_view(), name="register"),

]
