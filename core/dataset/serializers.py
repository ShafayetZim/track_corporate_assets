from rest_framework import serializers
from .models import *


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = '__all__'


class EmployeeSerializer(serializers.ModelSerializer):
    company_name = serializers.ReadOnlyField(source='company.name')
    device_info = DeviceSerializer(many=True, read_only=True, source='device')

    class Meta:
        model = Employee
        fields = ['id', 'user', 'device', 'company', 'company_name', 'device_info']


class AssetSerializer(serializers.ModelSerializer):
    device_name = serializers.ReadOnlyField(source='device.name')
    employee_name = serializers.ReadOnlyField(source='employee.name')

    class Meta:
        model = AssetLog
        fields = ['id', 'device', 'employee', 'checkout_date', 'return_date', 'device_name', 'employee_name']


class AssetReturnedSerializer(serializers.ModelSerializer):
    return_date = serializers.DateTimeField()

    class Meta:
        model = AssetLog
        fields = ['id', 'checkout_date', 'return_date']