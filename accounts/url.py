from django.urls import path
from .views import *
urlpatterns = [
    path('signup/',signup_view ,name="signup-page" ),
    path('login/',login_view ,name="login-page" ),
    path('logout/',logout_view ,name="logout-page" ),
]
