import os
import pandas as pd
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import seaborn as sns
import matplotlib.pyplot as plt

# Cargar las variables del archivo .env
load_dotenv()

# Obtener CLIENT_ID y CLIENT_SECRET del entorno
client_id = os.environ.get('CLIENT_ID')
client_secret = os.environ.get('CLIENT_SECRET')

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=client_id,
                                                           client_secret=client_secret))

artist_id = "4gzpq5DPGxSnKTe4SA8HAU"

response = sp.artist_top_tracks(artist_id)
if response:
    tracks = response["tracks"]
    tracks = [{k: (v / (1000 * 60)) % 60 if k == "duration_ms" else v for k, v in track.items()
               if k in ["name", "popularity", "duration_ms"]} for track in tracks]
    
tracks_df = pd.DataFrame.from_records(tracks)
tracks_df.sort_values(["popularity"], inplace=True)

print(tracks_df.tail())
