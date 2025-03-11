from django.contrib.gis.db import models


# class Activity(models.Model):
#     # from strava
#     pass
#     # polyine


# class Route(models.Model):
#     # aggregated route from strava data
#     pass
#     # polyline


class User(models.Model):
    strava_id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=255, null=True)
    last_name = models.CharField(max_length=255, null=True)
    user_name = models.CharField(max_length=255, null=True)
    gender = models.CharField(max_length=25, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    access_token = models.CharField(max_length=255)
    refresh_token = models.CharField(max_length=255)
    expires_at = models.IntegerField()  # epoch timestamp
