
# Create your models here.

from django.db import models

class TourCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Tour(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(TourCategory, related_name='tours', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

