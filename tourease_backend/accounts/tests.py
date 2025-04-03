
# Create your tests here.

from django.contrib.auth import get_user_model
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status

User = get_user_model()

class AuthenticationTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.register_url = "/api/accounts/register/"
        self.login_url = "/api/accounts/login/"
        self.profile_url = "/api/accounts/profile/"  # Example protected route

        self.user_data = {
            "username": "testuser",
            "email": "testuser@example.com",
            "password": "testpassword123"
        }

        # Create a test user
        self.user = User.objects.create_user(**self.user_data)

    def test_user_registration(self):
        """Test user can register successfully"""
        response = self.client.post(self.register_url, {
            "username": "newuser",
            "email": "newuser@example.com",
            "password": "securepassword123"
        }, format="json")

        print("Registration Response:", response.status_code, response.json())  # Debugging output
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn("username", response.data)

    def test_user_login(self):
        """Test user can log in and receive access & refresh tokens"""
        response = self.client.post(self.login_url, {
            "username": self.user_data["username"],
            "password": self.user_data["password"]
        }, format="json")

        print("Login Response:", response.status_code, response.json())  # Debugging output
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("access", response.data)
        self.assertIn("refresh", response.data)

    def test_access_protected_route(self):
        """Test access to a protected route with valid token"""
        # Log in first to get JWT token
        login_response = self.client.post(self.login_url, {
            "username": self.user_data["username"],
            "password": self.user_data["password"]
        }, format="json")

        token = login_response.data.get("access")
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')

        response = self.client.get(self.profile_url)

        print("Protected Route Response:", response.status_code, response.json())  # Debugging output
        self.assertEqual(response.status_code, status.HTTP_200_OK)

