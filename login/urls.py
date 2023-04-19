# from django.contrib.auth.views import LogoutView
# from django.urls import path
# from login.views import AccountLoginView, AccountRegisterView
#
# app_name = 'login'
#
# urlpatterns = [
#     path('login/', AccountLoginView.as_view(), name='login'),
#     path('logout/', LogoutView.as_view(), name='logout'),
#     path('signup/', AccountRegisterView.as_view(), name='signup'),
#
# ]

# from django.urls import path
# from login.views import SignUpView
#
# urlpatterns = [
#     path('signup/', SignUpView.as_view(), name='signup')
# ]

# from django.contrib.auth.views import LogoutView
# from django.urls import path
#
# from login.views import custom_login, profile, profile_edit, profile_delete, RegisterView
#
# app_name = "login"
#
# urlpatterns = [
#     path("login/", custom_login, name="login"),
#     path("logout/", LogoutView.as_view(), name="logout"),
#     path("profile/", profile, name="profile"),
#     # path("<int:pk>/edit/", UserProfileUpdate.as_view(), name="profile_edit"),
#     path("edit/", profile_edit, name="profile_edit"),
#     path("delete/", profile_delete, name="profile_delete"),
#     path("register/", RegisterView.as_view(), name="register")
# ]


# from django.contrib.auth.views import LogoutView
# from django.urls import path
#
# from login.views import RegisterView, custom_login, profile
#
# app_name = "account"
#
# urlpatterns = [
#     # path("login/", AccountLoginView.as_view(), name="login"),
#     path("login/", custom_login, name="login"),
#     path("logout/", LogoutView.as_view(), name="logout"),
#     path("profile/", profile, name="profile"),
#     path("sign_up/", RegisterView.as_view(), name="signup"),
#     # path("sign_up/", AccountSignupView.as_view(), name="sign_up")
# ]
from django.contrib.auth.views import LogoutView
from django.urls import path
from login.views import AccountLoginView, AccountRegisterView

app_name = 'login'

urlpatterns = [
    path('login/', AccountLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', AccountRegisterView.as_view(), name='signup'),

]
