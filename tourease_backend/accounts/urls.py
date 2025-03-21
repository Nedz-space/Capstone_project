from django.urls import path
from .views import RegisterAPIView, UserProfileAPIView
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('register/', RegisterAPIView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('profile/', UserProfileAPIView.as_view(), name='profile'),
]

