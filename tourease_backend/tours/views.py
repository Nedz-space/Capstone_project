
# Create your views here.

from rest_framework import generics
from .models import Tour, TourCategory
from .serializers import TourSerializer, TourCategorySerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class TourListCreateAPIView(generics.ListCreateAPIView):
    queryset = Tour.objects.all()
    serializer_class = TourSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class TourRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tour.objects.all()
    serializer_class = TourSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class TourCategoryListAPIView(generics.ListAPIView):
    queryset = TourCategory.objects.all()
    serializer_class = TourCategorySerializer

