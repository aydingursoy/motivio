from django.shortcuts import render, redirect
from .models import MaintenanceLog
from .forms import MaintenanceLogForm

def maintenance_log(request):
    if request.method == 'POST':
        form = MaintenanceLogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('maintenance_log')
    else:
        form = MaintenanceLogForm()
    logs = MaintenanceLog.objects.all()
    return render(request, 'maintenance/maintenance_log.html', {'form': form, 'logs': logs})
