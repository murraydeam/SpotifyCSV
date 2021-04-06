"""
# 1 Sign into Spotify
# 2 Get Playlist
# 3 Add song from Playlist to CSV
"""
import requests
import json
from pprint import pprint
from secrets import user_id, s_token


class PlaylistCSV:
    def __init__(self):
        pass

    def sign_in(self):  # User sign in to see saved playlists.
        pass

    def show_playlist(self):
        url = f'https://api.spotify.com/v1/users/{user_id}/playlists?limit=10&offset=5'
        request_body = ''
        response = requests.get(url,
                                data=request_body,
                                headers={
                                    "Accept": "application/json",
                                    "Content-Type": "application/json",
                                    "Authorization": f"Bearer {s_token}"
                                }
                                )

        pass

    def get_playlist(self):  # Focus a Specific Playlist
        pass


    def song_csv(self):  # Add the song to a CSV
        pass




