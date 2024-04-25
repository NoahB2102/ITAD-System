from django.db import models

class Device(models.Model):
    serial_number = models.CharField(max_length=255, unique=True)
    mac_address = models.CharField(max_length=255, unique=True, blank=True, null=True)
    device_type = models.CharField(max_length=100)
    purchase_date = models.DateField()
    last_service_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=100, default='active')  # z.B. active, retired, recycling
    condition = models.CharField(max_length=100, default='good')
    comments = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.serial_number
