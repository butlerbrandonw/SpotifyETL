# Import libraries
import psycopg2
import sqlalchemy
# Import project files
import extract

print("Starting load.py...")

# Create SQLAlchemy engine
engine = sqlalchemy.create_engine('postgresql://postgres:postgres@localhost/spotifyetl')

# Establish connection to local postgres database
con = psycopg2.connect(
    host = "localhost",
    database = "spotifyetl",
    user = "postgres",
    password = "postgres"
)

# Declare cursor
cur = con.cursor()

# Create table if it doesn't exist
sql_create_table = """
CREATE TABLE IF NOT EXISTS daily_played_tracks(
    song_name VARCHAR(200),
    artist_name VARCHAR(200),
    played_at VARCHAR(200) PRIMARY KEY,
    timestamp VARCHAR(200)  
)
"""

# Execute query to create table
cur.execute(sql_create_table)

# Execute query to insert into database
try:
    extract.song_df.to_sql("daily_played_tracks", engine, index=False, if_exists='append')
    print("Daily songs successfuly uploaded into database!")
except:
    print("Daily songs already uploaded to database.")

# Close cursor
cur.close()

# Commit changes
con.commit()

# Close connection
con.close()

print("Successfuly completed load.py!")