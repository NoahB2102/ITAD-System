from django import forms
from .models import Device

class DeviceForm(forms.ModelForm):
    class Meta:
        model = Device
        fields = ['serial_number', 'mac_address', 'device_type', 'purchase_date', 'last_service_date', 'status', 'condition', 'comments']
        