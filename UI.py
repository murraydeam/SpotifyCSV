"""
Greet
Prompt
Get info
Return Save Location
"""


def ui():
    count = 0
    print('Howdy, Please enter the Playlist ID.\n')
    playlistID = input('ID: ')
    print('Re-Enter Playlist ID')
    pConfirm = input('ID: ')
    count += 1
    print(f'{count}/5 tries...')

    while playlistID != pConfirm:
        print('Error, ID\'s do not match')
        playlistID = input('Try again.\nID: ')
        pConfirm = input('Confirm ID: ')
        count += 1
        print(f'{count}/5 tries...')
        if count >= 5:
            print('You Have Failed...')
            break


ui()
