
# Create your tests here.

from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from bookings.models import Booking
from tours.models import Tour
from django.contrib.auth import get_user_model

User = get_user_model()

class BookingsTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username="testuser", password="password123")
        self.tour = Tour.objects.create(name="City Tour", price=50.00)
        self.booking = Booking.objects.create(user=self.user, tour=self.tour, status="confirmed")
        self.client.force_authenticate(user=self.user)

    def test_create_booking(self):
        """Test creating a new booking"""
        response = self.client.post('/api/bookings/', {'tour': self.tour.id, 'status': 'pending'})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

