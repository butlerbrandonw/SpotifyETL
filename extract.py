# Import libraries
import pandas as pd
import requests
import json
import datetime

if __name__ == "__main__":
    
    raise Exception("Please call main.py, as it connects both transform.py and load.py as well.")

else:
    
    print("Starting extract.py...")
    
    SPOTIFY_USERNAME = "1279572017"
    SPOTIFY_TOKEN = "BQD4KneK2y0YlFZe3JUxJmWUcrPC3IUZ2hFHB_6pWW1UPmXu0RZdnbRKk0JQlUh9SdNGtXxV6nm83dE34Dp4deOCIsYn6XYi8v1OMR7UIjLSLVYGyrBl3ziD0ZtIexFN7GpNmEGtdXFQb64ZgwQ1"

    headers = {
        "Accept" : "application/json",
        "Content-Type" : "application/json",
        "Authorization" : "Bearer {token}".format(token=SPOTIFY_TOKEN)
    }
        
    today = datetime.datetime.now()
    yesterday = today - datetime.timedelta(days = 1)
    yesterday = yesterday.replace(hour=0, minute=0, second=0, microsecond=0)
    yesterday_unix_timestamp = int(yesterday.timestamp()) * 1000
        
    req = requests.get("https://api.spotify.com/v1/me/player/recently-played?after={time}".format(time=yesterday_unix_timestamp), headers = headers)
        
    data = req.json()
        
    song_names = []
    artist_names = []
    played_at_list = []
    timestamps = []

    # Extracting only the relevant bits of data from the json object      
    for song in data["items"]:
        song_names.append(song["track"]["name"])
        artist_names.append(song["track"]["album"]["artists"][0]["name"])
        played_at_list.append(song["played_at"])
        timestamps.append(song["played_at"][0:10])
            
    # Prepare a dictionary in order to turn it into a pandas dataframe below       
    song_dict = {
        "song_name" : song_names,
        "artist_name": artist_names,
        "played_at" : played_at_list,
        "timestamp" : timestamps
    }

    # Creatd pandas dataframe
    song_df = pd.DataFrame(song_dict, columns = ["song_name", "artist_name", "played_at", "timestamp"])
        
    print("Successfuly completed extract.py!")
    
    