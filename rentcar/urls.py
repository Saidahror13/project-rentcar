from django.urls import path
from rentcar.views import *

urlpatterns = [
    path('', CarListView.as_view(), name='homepage'),
    path('more/<int:pk>/', cardetail, name='more')
]
