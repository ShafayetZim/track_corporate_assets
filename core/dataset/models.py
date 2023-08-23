from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=255, help_text="Enter company name.")
    address = models.CharField(max_length=255, help_text="Enter company address.")
    phone = models.CharField(max_length=16, unique=True, help_text="Enter company phone.")

    class Meta:
        verbose_name_plural = 'Companies'
        ordering = ['-id']

    def __str__(self):
        return f'{self.name}'


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company = models.ForeignKey("Company", on_delete=models.CASCADE)
    device = models.ManyToManyField("Device", related_name='device_info')

    class Meta:
        verbose_name_plural = 'Employees'
        ordering = ['-id']

    def __str__(self):
        return f'{self.user.username}'


class Device(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, help_text="Enter device name.")
    device_code = models.CharField(max_length=255, unique=True)
    conditions = models.CharField(max_length=100, default='fresh', help_text="Condition of this device.")
    checked_out = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Devices'
        ordering = ['-id']

    def __str__(self):
        return f'{self.name}'


class AssetLog(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    checkout_date = models.DateTimeField(null=True, blank=True)
    return_date = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Asset Log'
        ordering = ['-updated_at']

    def __str__(self):
        return f'{self.device.name}'