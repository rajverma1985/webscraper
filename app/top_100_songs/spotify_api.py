import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv

load_dotenv()

# spotify dashboard: https://developer.spotify.com/dashboard/
# app name: billboard_top100
scope = "playlist-modify-private"
redirect_uri = "http://example.com"

sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
search_str = 'Muse'
result = sp.search(search_str)
print(result)

