import spotipy
import random
import json
from pathlib import Path
from itertools import islice
from spotipy.oauth2 import SpotifyOAuth

# Get users currently saved track IDs
def get_saved_tracks():
    print(f"Grabbing current liked songs..")
    playlists = sp.current_user_saved_tracks()
    counter = 1
    while playlists:
        for i, playlist in enumerate(playlists['items']):
            track = playlist['track']
            # print(counter, track['artists'][0]['name'], "–", track['name'], track['id'])
            saved_track_ids.append(track['id'])
            counter += 1
        if playlists['next']: #paginate
            playlists = sp.next(playlists)
        else:
            playlists = None
    print(f"Got {len(saved_track_ids)} tracks!")

# Lookup playlist id by name
def find_playlist_id(playlists):
    playlistID = ''
    for i, item in enumerate(playlists['items']):
        if item['name'] == randomized_playlist_name:
            playlistID = item['id']
    return playlistID

# Delete existing playlist if it exists
def delete_playlist():
    randomized_playlist_ID = find_playlist_id(sp.user_playlists(sp.me()['id']))
    if randomized_playlist_ID:
        sp.user_playlist_unfollow(sp.me()['id'], randomized_playlist_ID) 

# Create new spotify playlist
def create_playlist():
    new_playlist_id = sp.user_playlist_create(sp.me()['id'], randomized_playlist_name, public=False, collaborative=False, description="Random playlist created by spotify-randomizer")

    # Shuffle songs
    print('Shuffling songs!')
    random.shuffle(saved_track_ids)

    # Add tracks to new playlist in chunks of 100
    print(f'Creating new {randomized_playlist_name} playlist..')
    iterator = iter(saved_track_ids)
    while chunk := list(islice(iterator, 100)):
        sp.user_playlist_add_tracks(sp.me(), new_playlist_id['id'], chunk)


if __name__ == "__main__":
    config_file = Path(".spotifyapp")
    if config_file.is_file():
        with open('.spotifyapp', 'r') as f:
            config = json.load(f)
    else:
        print('Please [Create a Spotify app](https://developer.spotify.com/dashboard)')
        data = {}
        data['client_id'] = input('Enter your client ID: ')
        data['client_secret'] = input('Enter your client secret: ')
        with open('.spotifyapp', 'w') as outfile:
            json.dump(data, outfile)

        print('Please run this script again.')
        exit()

    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=config["client_id"],
                                                client_secret=config["client_secret"],
                                                redirect_uri="https://rsmail.co",
                                                scope="user-library-read, playlist-read-private, playlist-modify-private, playlist-modify-public",
                                                open_browser=False))

    randomized_playlist_name = 'Randomized Playlist'
    saved_track_ids = []
    get_saved_tracks()
    delete_playlist()
    create_playlist()
    print('Done!')