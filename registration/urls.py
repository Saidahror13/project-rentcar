from django.contrib.auth.views import LogoutView
from django.urls import path

from registration.views import custom_login, profile, profile_edit, profile_delete, RegisterView

app_name = "registration"

urlpatterns = [
    path("registration/", custom_login, name="registration"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("profile/", profile, name="profile"),
    # path("<int:pk>/edit/", UserProfileUpdate.as_view(), name="profile_edit"),
    path("edit/", profile_edit, name="profile_edit"),
    path("delete/", profile_delete, name="profile_delete"),
    path("signup/", RegisterView.as_view(), name="signup")
]


# from django.contrib.auth.views import LogoutView
# from django.urls import path
# from registration.views import AccountLoginView, AccountRegisterView
#
# app_name = 'registration'
#
# urlpatterns = [#     path('registration/', AccountLoginView.as_view(), name='registration'),
#     path('logout/', LogoutView.as_view(), name='logout'),
#     path('signup/', AccountRegisterView.as_view(), name='signup'),
#
# ]
