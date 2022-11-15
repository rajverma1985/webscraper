import os

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv

load_dotenv()

# spotify dashboard: https://developer.spotify.com/dashboard/
# app name: billboard_top100

client_id = os.environ.get('client_ID')
client_secret = os.environ.get('Client_Secret')

birdy_uri = ''
spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
