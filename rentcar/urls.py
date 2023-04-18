from django.urls import path
from rentcar.views import *

urlpatterns = [
    path('', CarListView.as_view(), name='homepage'),
    path('more/<int:pk>/', cardetail, name='more'),
    path('categories/', CarCategories.as_view(), name='categories'),
    path('buy/<int:pk>/', BuyNow.as_view(), name='buy'),
    path('discount/', Discount.as_view(), name='discount'),
]
