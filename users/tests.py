from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

class UserViewTests(TestCase):
    def test_register_page(self):
        response = self.client.get(reverse('users:register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/register.html')

    def test_login_page(self):
        response = self.client.get(reverse('users:login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/login.html')

    def test_profile_page_requires_login(self):
        response = self.client.get(reverse('users:profile'))
        self.assertEqual(response.status_code, 302)  # Redirect to login page

    def test_user_registration(self):
        response = self.client.post(reverse('users:register'), {
            'username': 'testuser',
            'password1': 'complexpassword123',
            'password2': 'complexpassword123'
        })
        self.assertEqual(response.status_code, 302)  # Redirect after successful registration
        self.assertTrue(User.objects.filter(username='testuser').exists())

class UserModelTests(TestCase):
    def test_user_creation(self):
        user = User.objects.create_user(username='testuser', password='complexpassword123')
        self.assertEqual(user.username, 'testuser')

