from django.shortcuts import render

# Create your views here.

from django.contrib.auth.views import LoginView
from login.forms import CustomAuthenticationForm


class AccountLoginView(LoginView):
    form_class = CustomAuthenticationForm
    template_name = 'login/login.html'

