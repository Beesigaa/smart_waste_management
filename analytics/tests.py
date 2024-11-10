from django.test import TestCase
from django.urls import reverse

class AnalyticsViewTests(TestCase):
    def test_dashboard_page(self):
        response = self.client.get(reverse('analytics:dashboard'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "Dashboard")

