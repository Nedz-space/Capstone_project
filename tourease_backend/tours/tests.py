
# Create your tests here.

from django.contrib.auth import get_user_model
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from tours.models import Tour, TourCategory
from rest_framework_simplejwt.tokens import RefreshToken  # Import JWT tokens

User = get_user_model()

class ToursTestCase(TestCase):
    def setUp(self):
        """Set up a test user, category, and tour with authentication."""
        self.client = APIClient()

        # Create test user
        self.user = User.objects.create_user(username="testuser", password="password123")

        # Generate JWT token for the test user
        refresh = RefreshToken.for_user(self.user)
        self.access_token = str(refresh.access_token)

        # Authenticate client
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')

        # Create test category and tour
        self.category = TourCategory.objects.create(name="Adventure")
        self.tour = Tour.objects.create(
            title="Safari Adventure",
            description="A thrilling safari experience",
            location="Kenya",
            price=100.00,
            category=self.category
        )

    def test_get_tours(self):
        """Test retrieving a list of tours"""
        response = self.client.get('/api/tours/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_get_tour_detail(self):
        """Test retrieving a single tour"""
        response = self.client.get(f'/api/tours/{self.tour.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Safari Adventure")

    def test_create_tour(self):
        """Test creating a new tour (requires authentication)"""
        response = self.client.post('/api/tours/', {
            "title": "Mountain Trekking",
            "description": "Hiking in the mountains",
            "location": "Tanzania",
            "price": 150.00,
            "category": self.category.id
        }, format='json')

        print(f"Create Tour Response: {response.status_code} {response.data}")  # Debugging

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["title"], "Mountain Trekking")

    def test_update_tour(self):
        """Test updating an existing tour (requires authentication)"""
        response = self.client.patch(f'/api/tours/{self.tour.id}/', {
            "price": 120.00
        }, format='json')

        print(f"Update Tour Response: {response.status_code} {response.data}")  # Debugging

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(float(response.data["price"]), 120.00)

    def test_delete_tour(self):
        """Test deleting a tour (requires authentication)"""
        response = self.client.delete(f'/api/tours/{self.tour.id}/')

        print(f"Delete Tour Response: {response.status_code}")  # Debugging

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Ensure it no longer exists
        response = self.client.get(f'/api/tours/{self.tour.id}/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

