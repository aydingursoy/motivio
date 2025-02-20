from django.shortcuts import render, redirect
from .models import Vehicle
from .forms import VehicleForm

from django.contrib.auth.decorators import login_required

@login_required
def vehicle_profile(request):
    if request.method == 'POST':
        form = VehicleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vehicle_profile')
    else:
        form = VehicleForm()
    vehicles = Vehicle.objects.all()
    return render(request, 'vehicles/vehicle_profile.html', {'form': form, 'vehicles': vehicles})

