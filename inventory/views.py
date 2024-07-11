from django.shortcuts import render, redirect
from .models import Hardware
from .forms import HardwareForm

def hardware_list(request):
    hardwares = Hardware.objects.all()
    return render(request, 'inventory/hardware_list.html', {'hardwares': hardwares})

def add_hardware(request):
    if request.method == 'POST':
        form = HardwareForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('hardware_list')
    else:
        form = HardwareForm()
    return render(request, 'inventory/add_hardware.html', {'form': form})
