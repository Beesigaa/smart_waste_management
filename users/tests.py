# users/tests.py
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

class UserViewTests(TestCase):
    def test_login_page(self):
        response = self.client.get(reverse('users:login'))
        self.assertEqual(response.status_code, 200)

    def test_register_page(self):
        response = self.client.get(reverse('users:register'))
        self.assertEqual(response.status_code, 200)

    def test_profile_page_requires_login(self):
        response = self.client.get(reverse('users:profile'))
        self.assertRedirects(response, '/users/login/?next=/users/profile/')  # Adjust based on your login URL

    def test_user_registration(self):
        response = self.client.post(reverse('users:register'), {
            'username': 'testuser',
            'email': 'test@example.com',
            'password1': 'complexpassword123',
            'password2': 'complexpassword123'
        })
        self.assertEqual(response.status_code, 302)  # Redirect after successful registration
        self.assertTrue(User.objects.filter(username='testuser').exists())

