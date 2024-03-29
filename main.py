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
import csv


class PlaylistCSV:
    def __init__(self):
        self.allData = []
        self.token = self.auth_token
        self.offset = 0
        self.count = 0

    def auth_token(self):  # client auth for application
        # URL where the post request will be sent
        # Post Requests
        url = 'https://accounts.spotify.com/api/token'

        # The request variables as dictionary's
        headers = {}
        data = {}

        # The Requests message
        # formatted for ease while converting to BASE64
        message = f'{client_id}:{client_secret}'

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
        self.token = r.json()['access_token']
        return self.token

    def show_playlist(self):  # Show the user all their playlists.
        # Step 2 - Use Access Token to call playlist endpoint

        # playlistId = "0dc6pAFmZfOCyQ6u0pC91Y"  # **Streamline for ease of use**
        playlistId = input(
            'There is currently a max playlist size of 62. \nPlease enter you playlist ID: ')

        if playlistId == '':
            print('\nShoot an Email to dmurray@brinkshome.com '
                  'if you have any questions.')
            playlistId = '0dc6pAFmZfOCyQ6u0pC91Y'
        else:
            playlistId = playlistId
        playlistUrl = f"https://api.spotify.com/v1/playlists/{playlistId}" \
                      f"/tracks?market=us&limit=100&offset={self.offset}"
        headers = {
            "Authorization": "Bearer " + str(self.token)
        }
        res = requests.get(url=playlistUrl, headers=headers)
        playlist_data = json.dumps(res.json())
        playlist_data = json.loads(playlist_data)

        # Define Var as a list

        for album in playlist_data['items']:
            for artist in album['track']['album']['artists']:
                #  Get data from the spotify Json (Song name, Artist, Album Name)
                albumName = album['track']['name'].replace(',', '')
                trackName = album['track']['album']['name'].replace(',', '')
                artistName = artist['name'].replace(',', '')
                trackData = [albumName, trackName, artistName]
                # The above will also remove any Comma's from the data for simple csv parsing.
                # Append 'trackData' to list 'allData'
                self.allData.append(trackData)
                self.count += 1

        return self.allData

    @staticmethod
    def songs_csv():  # Add Song to a CSV
        allData = ans.show_playlist()
        fields = ['Title', 'Artist', 'Album']

        with open(playlistID + '.csv', 'w', newline='') as csvFile:
            write = csv.writer(csvFile)

            write.writerow(fields)
            write.writerows(allData)


ans = PlaylistCSV()
link_token = ans.auth_token()
ans.songs_csv()
