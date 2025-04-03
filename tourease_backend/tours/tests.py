
# Create your tests here.

from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from tours.models import Tour

class ToursTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.tour = Tour.objects.create(name="Safari Adventure", price=100.00)

    def test_get_tours(self):
        """Test retrieving list of tours"""
        response = self.client.get('/api/tours/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

