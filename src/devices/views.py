from django.shortcuts import render, redirect
from .forms import DeviceForm
from .models import Device

def device_create_view(request):
    form = DeviceForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('device-list')
    return render(request, 'devices/device_form.html', {'form': form})

def device_list_view(request):
    devices = Device.objects.all()
    return render(request, 'devices/device_list.html', {'devices': devices})