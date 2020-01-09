from django.contrib import admin
from django.urls import path
from .views import mnistfunc

urlpatterns = [
    path('mnist/',mnistfunc,name = 'mnist'),
]
