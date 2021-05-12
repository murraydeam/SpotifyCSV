import pprint
import ijson
import csv
import requests
import base64
import json
from secrets import *

# Step 1 - Authorization
"""
Line 14 -
"""

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
fields = ['Title', 'Artist', 'Album']

for album in playlist_data['tracks']['items']:
    for artist in album['track']['album']['artists']:
        #  Get data from the spotify Json (Song name, Artist, Album Name)
        albumName = album['track']['album']['name']
        songName = album['track']['name']
        artistName = artist['name']

        #  print(f'\n{songName} by {artistName}\nAlbum : {albumName}')

        datas = 'Song Name: ' + songName + '\nArtist Name: ' + artistName + '\nAlbum Name: ' + albumName
        print('\n' + datas)
with open(playlistID + '.csv', 'w', newline='') as csvfile:
    songwriter = csv.writer(csvfile, delimiter=' ')
"""
for artist in playlist_data['tracks']['items']:
    print(artist['track']['name'])
"""

