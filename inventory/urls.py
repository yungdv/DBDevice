from django.urls import path
from . import views

urlpatterns = [
    path('', views.hardware_list, name='hardware_list'),
    path('add/', views.add_hardware, name='add_hardware'),
]
