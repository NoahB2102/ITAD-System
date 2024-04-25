from django.urls import path
from .views import device_create_view, device_list_view

urlpatterns = [
    path('create/', device_create_view, name='device-create'),
    path('list/', device_list_view, name='device-list'),
]