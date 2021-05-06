import pprint
import ijson

import requests
import base64
import json
from secrets import *

# Step 1 - Authorization
url = "https://accounts.spotify.com/api/token"
headers = {}
data = {}

# Encode as Base64
message = f"{client_id}:{client_secret}"
messageBytes = message.encode('ascii')
base64Bytes = base64.b64encode(messageBytes)
base64Message = base64Bytes.decode('ascii')


headers['Authorization'] = f"Basic {base64Message}"

data['grant_type'] = "client_credentials"

r = requests.post(url, headers=headers, data=data)

token = r.json()['access_token']

# Step 2 - Use Access Token to call playlist endpoint

playlistId = "0dc6pAFmZfOCyQ6u0pC91Y"
playlistUrl = f"https://api.spotify.com/v1/playlists/{playlistId}"
headers = {
    "Authorization": "Bearer " + token
}

res = requests.get(url=playlistUrl, headers=headers)
playlist_data = json.dumps(res.json())
playlist_data = json.loads(playlist_data)
"""
for key in playlist_data['tracks'].keys():
    print(key)
"""
# del playlist_data['tracks']['items']

for album in playlist_data['tracks']['items']:
    for artist in album['track']['album']['artists']:
        print(album['track']['name'] + ' : ' + artist['name'])



"""
for artist in playlist_data['tracks']['items']:
    print(artist['track']['name'])
"""


