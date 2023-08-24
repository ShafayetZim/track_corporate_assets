from django.contrib import admin
from .models import Employee, Company, Device, AssetLog


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('user', 'company')
    search_fields = ('user', 'company', 'device')
    list_filter = ('company', 'device')


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'address')
    search_fields = ('name', 'phone', 'address')
    list_filter = ('phone', 'address')


@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ('name', 'company', 'device_code', 'checked_out')
    search_fields = ('name', 'device_code', 'company__name')
    list_filter = ('device_code', 'company', 'checked_out')
    list_editable = ('checked_out',)
    date_hierarchy = 'created_at'


@admin.register(AssetLog)
class AssetLogAdmin(admin.ModelAdmin):
    list_display = ('device', 'employee', 'checkout_date', 'return_date')
    search_fields = ('company__name',)
    date_hierarchy = 'checkout_date'
