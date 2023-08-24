from django.urls import path
from .views import CompanyCreateView, CompanyListView, CompanyUpdateView, \
    EmployeeAPIView, EmployeeRetrieveUpdateDestroyView, EmployeesAssignedDeviceListView, \
    AssetLogCreateView, AssetLogRetrieveUpdateDestroyView, AssetLogListView, \
    DeviceStatusView

urlpatterns = [
    path('create-company/', CompanyCreateView.as_view(), name='create-company'),
    path('update-company/<int:pk>/', CompanyUpdateView.as_view(), name='update-company'),
    path('company-list/', CompanyListView.as_view(), name='view-all-company-list'),

    path('employees-api/', EmployeeAPIView.as_view(), name='employee-list'),
    path('employees-api/<int:pk>/', EmployeeAPIView.as_view(), name='employee-detail'),
    path('employees/<int:pk>/', EmployeeRetrieveUpdateDestroyView.as_view(), name='employee-rud'),
    # rud=RetrieveUpdateDestroy

    path('create-asset-log/', AssetLogCreateView.as_view(), name='create-asset-log'),
    path('asset-log/<int:pk>/', AssetLogRetrieveUpdateDestroyView.as_view(), name='asset-log-rud'),
    path('employees-assigned-devices/', EmployeesAssignedDeviceListView.as_view(),
         name='employees-assigned-list'),

    path('all-assigned-device-list/', AssetLogListView.as_view(), name='all-assigned-device-list'),

    path('device-status/', DeviceStatusView.as_view({'get': 'list'}), name='device-status'),
]
