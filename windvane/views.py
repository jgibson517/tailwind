from django.shortcuts import render
from django.http import Http404

from .strava import get_access_token
from .models import User
from requests import HTTPError


# Create your views here.

# route-finder
# takes strava activity data -> groups similar routes together to
# show user their common routes
# user then selects routes they wish to track
# weather analysis is conducted on these routes


def authorize_user(request):
    ### redirect logic goes here
    ## need landing page if users don't authorize
    auth_token = ""

    try:
        auth_resp = get_access_token(auth_token)
    except HTTPError:
        raise Http404

    athlete = auth_resp["athlete"]

    new_user = User(
        strava_id=athlete["id"],
        first_name=athlete["firstname"],
        last_name=athlete["lastname"],
        user_name=athlete["username"],
        gender=athlete["sex"],
        access_token=auth_resp["access_token"],
        refresh_token=auth_resp["refresh_token"],
        expires_at=auth_resp["expires_at"],
    )

    # add to db
    new_user.save()

    context = {"user_name": f"{new_user.first_name} {new_user.last_name}"}
    return render(request, "windvane/new_user.html", context)
