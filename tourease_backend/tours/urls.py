
from django.urls import path
from .views import (
    TourListCreateAPIView,
    TourRetrieveUpdateDestroyAPIView,
    TourCategoryListAPIView,
    TourListView
)

urlpatterns = [
    path('', TourListCreateAPIView.as_view(), name='tour_list_create'),
    path('<int:pk>/', TourRetrieveUpdateDestroyAPIView.as_view(), name='tour_detail'),
    path('categories/', TourCategoryListAPIView.as_view(), name='category_list'),
    path('list/', TourListView.as_view(), name='tour-list'),
]

