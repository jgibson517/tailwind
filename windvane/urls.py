from django.urls import path
from . import views

urlpatterns = [
    path("", views.authorize_user, name="home"),
]
