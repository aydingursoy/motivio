from django.db import models
from vehicles.models import Vehicle

class MaintenanceLog(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    service_type = models.CharField(max_length=100)
    service_date = models.DateField()
    mileage = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)  # Add this line
    notes = models.TextField(blank=True, null=True)
    receipt_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"{self.service_type} on {self.service_date}"
