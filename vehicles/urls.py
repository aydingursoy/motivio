from django.urls import path
from . import views

urlpatterns = [
    path('', views.vehicle_profile, name='vehicle_profile'),
]
