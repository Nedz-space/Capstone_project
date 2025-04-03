
# Create your tests here.

from django.contrib.auth import get_user_model
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status

User = get_user_model()

class AccountsTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username="testuser", password="password123")
        self.client.force_authenticate(user=self.user)

    def test_user_creation(self):
        """Test user creation via API"""
        response = self.client.post('/register/', {
            'username': 'newuser',
            'password': 'securepass123'
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

