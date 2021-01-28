import sqlalchemy
import psycopg2
import pandas as pd
import requests
import json
import datetime

SPOTIFY_USERNAME = "1279572017"
SPOTIFY_TOKEN = "BQAoSEdJaeLMTXh__Yj5xqnkdLw0PMbc7gC96ZT0iRMs7ovuB910V3gvgj1-x5j9qCbaNTlVUTJlOFQKeCR8z_VGXHkWwwi2ArDq6PHw8-6Irfl6Uis5nq6L2VnWXSLMaKEQq5tUFsZeEqR1iKlM"
 
''' 
#establish connection to local postgres database
con = psycopg2.connect(
    host = "localhost",
    database = "spotifyetl",
    user = "postgres",
    password = "postgres"
    )

#declare cursor
cur = con.cursor()

#close cursor
cur.close()

#close connection
con.close()
'''

if __name__ == "__main__":
    
    headers = {
        "Accept" : "application/json",
        "Content-Type" : "application/json",
        "Authorization" : "Bearer {token}".format(token=SPOTIFY_TOKEN)
    }
    
    today = datetime.datetime.now()
    yesterday = today - datetime.timedelta(days = 1)
    yesterday_unix_timestamp = int(yesterday.timestamp()) * 1000
    
    req = requests.get("https://api.spotify.com/v1/me/player/recently-played?after={time}".format(time=yesterday_unix_timestamp), headers = headers)
    
    data = req.json()
    
    print(data)
    
