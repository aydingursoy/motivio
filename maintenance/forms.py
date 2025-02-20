from django import forms
from .models import MaintenanceLog

class MaintenanceLogForm(forms.ModelForm):
    class Meta:
        model = MaintenanceLog
        fields = ['vehicle', 'service_type', 'service_date', 'mileage', 'price', 'notes', 'receipt_url']
