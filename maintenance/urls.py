from django.urls import path
from . import views

urlpatterns = [
    path('', views.maintenance_log, name='maintenance_log'),
]
