from django.contrib.auth.views import LogoutView
from django.urls import path
from login.views import AccountLoginView,AccountRegisterView

app_name = 'login'

urlpatterns = [
    path('login/', AccountLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', AccountRegisterView.as_view(), name='signup'),

]

# from django.urls import path
# from .views import SignUpView
#
# urlpatterns = [
#     path('signup/', SignUpView.as_view(), name='signup')
# ]
