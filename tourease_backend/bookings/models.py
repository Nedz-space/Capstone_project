
# Create your models here.

from django.db import models
from django.contrib.auth import get_user_model
from tours.models import Tour

User = get_user_model()

class Booking(models.Model):
    user = models.ForeignKey(User, related_name='bookings', on_delete=models.CASCADE)
    tour = models.ForeignKey(Tour, related_name='bookings', on_delete=models.CASCADE)
    date = models.DateField()
    number_of_people = models.PositiveIntegerField()
    booked_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Booking by {self.user.username} for {self.tour.title}'

