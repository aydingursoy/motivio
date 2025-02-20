from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView  # Add this line
from vehicles.views import vehicle_profile

urlpatterns = [
    path('admin/', admin.site.urls),
    path('vehicles/', include('vehicles.urls')),  # Add missing closing parenthesis
    path('maintenance/', include('maintenance.urls')),  # Add missing closing parenthesis
    path('', RedirectView.as_view(url='/vehicles/')),  # Redirect root to /vehicles/
     path('accounts/', include('allauth.urls')),
]
