import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
from billboard import song_list, date

load_dotenv()

# spotify dashboard: https://developer.spotify.com/dashboard/
# app name: billboard_top100


sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    scope="playlist-modify-private",
    redirect_uri="http://localhost:8888/callback",
    client_id=os.environ.get('SPOTIPY_CLIENT_ID'),
    client_secret=os.environ.get('SPOTIPY_CLIENT_SECRET'),
    show_dialog=True,
    cache_path="token.txt"
))

user_id = sp.current_user()["id"]
year = date.split("-")[0]
song_uris = []
for song in song_list:
    result = sp.search(q=f"track:{song} year:{year}")
    try:
        # get the uri so that we can add it to the playlist.
        uri = result['tracks']['items'][0]['uri']
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in spotify!")

# Creating a new private playlist in Spotify based on date
playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)

# # Adding songs to the playlist, passes the playlist id and uri for the song and adds it to the playlist
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
