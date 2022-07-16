from django.urls import path
from .views import *
urlpatterns = [
    # path('signup/',signup_view ,name="signup-page" ),
    path('feed/',feed_view ,name="feed-page" ),
    path('review/',review_view ,name="review-page" ),
    path('',home_view ,name="home-page" ),
    path('about/',about_view ,name="about-page" ),
]
