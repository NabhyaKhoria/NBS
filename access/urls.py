from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('hello',views.hello, name='hello'),
    path('buy',views.buy, name='buy'),
    path('sell',views.sell, name='sell'),
    path('logout',views.logout, name='logout'),
]

