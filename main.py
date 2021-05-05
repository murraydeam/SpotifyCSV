"""
*** IMPORTS ***
base64, requests, json
from secrets import *



# 1 get Auth for the application.
# 2 Get user info/sign in
# 3 Get user playlists
# 4 Get songs from playlist
# 5 Write songs to CSV
"""
import requests
import json
import base64
from secrets import *


class PlaylistCSV:
    def __init__(self):
        self.token = self.auth_token

    def auth_token(self):  # client auth for application
        # URL where the post request will be sent
        # Post Requests
        url = 'https://accounts.spotify.com/api/token'

        # The request variables as dictionary's
        headers = {}
        data = {}

        # The Requests message
        message = f'{client_id}:{client_secret}'  # formatted for ease while converting to BASE64

        # Encoding message BASE64
        messageBytes = message.encode('ascii')
        base64Bytes = base64.b64encode(messageBytes)

        # Decoding message
        base64Message = base64Bytes.decode('ascii')

        # Recomposing message after encoding
        headers['Authorization'] = f'Basic {base64Message}'
        data['grant_type'] = 'client_credentials'

        r = requests.post(url, headers=headers, data=data)

        # Get and store the token
        token = r.json()['access_token']
        return token
    auth_token(self)

    def sign_in(self):  # sign into spotify.
        # Get requests
        token = self.token
        params = {}
        url = 'https://accounts.spotify.com/authorize'
        r = requests.get(url, params=params)
        print(token)

    def show_playlist(self):  # Show the user all their playlists.
        pass

    def get_songs(self):  # Retrieve Songs from playlist selected
        pass

    def songs_csv(self):  # Add Song to a CSV
        pass

