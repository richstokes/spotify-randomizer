For when you want to randomize your saved songs into a new playlist.

This script takes your "Liked Songs", and shuffles their order into a new playlist. I made this because [Spotify's shuffle](https://medium.com/immensity/how-spotifys-shuffle-algorithm-works-19e963e75171) isn't totally random and was interested in the results :-)

## Setup
1. `pip3 install -r requirements.txt`
2. [Create a Spotify app](https://developer.spotify.com/dashboard), and set the `client_id` and `client_secret` when prompted
3. Optionally, edit the `randomized_playlist_name` variable in the script -- this will be wiped/recreated each time you run this sript


## Usage
`python3 sr.py`  

The first time you run, it will ask you to open a URL, and then require you to paste in the URL you are redirected to. It's fine if this redirect goes somewhere non-existent / 404s. 

