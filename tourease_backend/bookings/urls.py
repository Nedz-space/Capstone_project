from django.urls import path
from .views import (
    BookingCreateAPIView,
    UserBookingsListAPIView,
    BookingDeleteAPIView
)

urlpatterns = [
    path('bookings/', BookingCreateAPIView.as_view(), name='booking_create'),
    path('bookings/list/', UserBookingsListAPIView.as_view(), name='booking_list'),
    path('bookings/<int:pk>/', BookingDeleteAPIView.as_view(), name='booking_delete'),
]

