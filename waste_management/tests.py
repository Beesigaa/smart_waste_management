from django.test import TestCase
from django.urls import reverse
from waste_management.models import WasteBin, WasteRequest

class WasteManagementViewTests(TestCase):
    def test_waste_request_page(self):
        response = self.client.get(reverse('waste_management:request'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'waste_management/request.html')

    def test_full_bin_alert(self):
        full_bin = WasteBin.objects.create(is_full=True)
        response = self.client.get(reverse('waste_management:full_bin_alert'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Bin is full")

class WasteManagementModelTests(TestCase):
    def test_waste_bin_creation(self):
        waste_bin = WasteBin.objects.create(is_full=False)
        self.assertFalse(waste_bin.is_full)

    def test_waste_request_creation(self):
        waste_bin = WasteBin.objects.create(is_full=False)
        request = WasteRequest.objects.create(bin=waste_bin, request_type="collection")
        self.assertEqual(request.request_type, "collection")
        self.assertEqual(request.bin, waste_bin)

