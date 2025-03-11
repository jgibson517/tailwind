from django.urls import path
from . import views

urlpatterns = [
    path("exchange_token", views.authorize_user, name="authorize"),
    path("new_user", views.connect_strava, name="Connect with Strava"),
]
