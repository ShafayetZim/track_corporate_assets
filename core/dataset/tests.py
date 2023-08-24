from django.test import TestCase
from django.contrib.auth.models import User
from .models import Company, Employee, Device, AssetLog

class ModelTestCase(TestCase):

    def setUp(self):
        # Create a user for testing
        self.user = User.objects.create_user(username='testuser', password='testpassword')

        # Create a company for testing
        self.company = Company.objects.create(name='Test Company', address='Test Address', phone='1234567890')

        # Create an employee for testing
        self.employee = Employee.objects.create(user=self.user, company=self.company)

        # Create a device for testing
        self.device = Device.objects.create(company=self.company, name='Test Device', device_code='ABC123')

        # Create an asset log entry for testing
        self.asset_log = AssetLog.objects.create(device=self.device, employee=self.employee)

    def test_company_creation(self):
        self.assertEqual(str(self.company), 'Test Company')

    def test_employee_creation(self):
        self.assertEqual(str(self.employee), 'testuser')

    def test_device_creation(self):
        self.assertEqual(str(self.device), 'Test Device')

    def test_asset_log_creation(self):
        self.assertEqual(str(self.asset_log), 'Test Device')
