from django.urls import path
from .views import (
    BookingCreateAPIView,
    UserBookingsListAPIView,
    BookingDeleteAPIView
)

urlpatterns = [
    path('', BookingCreateAPIView.as_view(), name='booking_create'),
    path('list/', UserBookingsListAPIView.as_view(), name='booking_list'),
    path('<int:pk>/', BookingDeleteAPIView.as_view(), name='booking_delete'),
]

