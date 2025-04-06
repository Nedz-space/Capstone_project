TourEase - A Django-Powered Tour Booking API by Nedz

TourEase is a backend API built with Django and Django REST Framework to help users explore, filter, and book tours easily. It supports user authentication using JWT, tour categorization, booking, and includes search/filtering capabilities. The API is deployed on AWS EC2 and is production-ready.

Project Features
Accounts App
    User Registration
    JWT Login & Token Authentication (via SimpleJWT)
    User Profile Retrieval
Tours App
    CRUD for Tour Listings (Create, Read, Update, Delete)
    Tour Categories
    Filter Tours by Category or Location (optional improvements)
Bookings App
    Make a Tour Booking
    View User's Own Bookings
    Cancel a Booking

- Unit Testing for core features
- Deployed on AWS EC2 with Nginx and Gunicorn


 Tech Stack

- Backend: Django, Django REST Framework
- Authentication: JWT via djangorestframework-simplejwt
- Filtering: django-filter
- Database: PostgreSQL (or SQLite for development)
- Deployment: AWS EC2, Gunicorn, Nginx
- Testing: Django TestCase, DRF APITestCase

Virtual Environment
- python -m venv venv
- source venv/bin/activate  # On Windows: venv\Scripts\activate
- pip install -r requirements.txt

Built With

- Python
- Django
- Django REST Framework
- Gunicorn + Nginx
- Amazon EC2 (Ubuntu)
- Postman (API Testing)

