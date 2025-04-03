
# Create your tests here.

from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from tours.models import Tour, TourCategory

class ToursTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
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

