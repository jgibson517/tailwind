# wrapper for strava api
from dotenv import load_dotenv
from requests import Session
import os


load_dotenv()

AUTH_URL = "https://www.strava.com/oauth"
CLIENT_ID = os.getenv("STRAVA_CLIENT_ID")
CLIENT_SECRET = os.getenv("STRAVA_CLIENT_SECRET")

session = Session()


def get_access_token(auth_token: str) -> dict:
    """Get access token for first time users"""
    params = {
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "code": auth_token,
        "grant_type": "authorization_code",
    }
    resp = session.post(f"{AUTH_URL}/token", params=params)

    resp.raise_for_status()

    return resp.json()


def refresh_token(token: str) -> dict:
    """Refresh access token for users"""
    params = {
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "refresh_token": token,
        "grant_type": "refresh_token",
    }
    resp = session.post(f"{AUTH_URL}/token", params=params)

    resp.raise_for_status()

    return resp.json()
