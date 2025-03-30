import django_filters
from .models import Tour

class TourFilter(django_filters.FilterSet):
    category = django_filters.CharFilter(field_name="category__name", lookup_expr="icontains")  # Filtering by category name
    location = django_filters.CharFilter(field_name="location", lookup_expr="icontains")  # Case-insensitive match
    min_price = django_filters.NumberFilter(field_name="price", lookup_expr="gte")  # Greater than or equal to
    max_price = django_filters.NumberFilter(field_name="price", lookup_expr="lte")  # Less than or equal to

    class Meta:
        model = Tour
        fields = ['category', 'location', 'min_price', 'max_price']

