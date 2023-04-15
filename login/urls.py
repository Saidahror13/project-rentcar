from django.contrib.auth.views import LogoutView
from django.urls import path
from login.views import AccountLoginView

app_name = 'login'

urlpatterns = [
    path('login/', AccountLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout')
]


