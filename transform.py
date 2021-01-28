# Import libraries
import pandas as pd
import datetime
# Import project files
import extract

if __name__ == "__main__":
    
    raise Exception("Please call main.py, as it connects both extract.py and load.py as well.")

else:

    print("Starting transform.py...")

    def check_if_valid_data(df: pd.DataFrame) -> bool:
        # Check if dataframe is empty
        if df.empty:
            print("No songs downloaded.")
            return False
        
        # Check Primary Key
        if pd.Series(df['played_at']).is_unique:
            pass
        else:
            raise Exception("Primary Key (time song is played at) is duplicated.")
        
        # Check for nulls
        if df.isnull().values.any():
            raise Exception("Null values found in dataframe.")
        
        #Check dates to verify download is for yesterday
        yesterday = datetime.datetime.now() - datetime.timedelta(days = 1)
        yesterday = yesterday.replace(hour=0, minute=0, second=0, microsecond=0)
        
        timestamps = df["timestamp"].tolist()
        for timestamp in timestamps:
            if datetime.datetime.strptime(timestamp, '%Y-%m-%d') != yesterday:
                raise Exception("At least one of the returned songs does not have yesterday's timestamp.")
        
        return True
    
    if check_if_valid_data(extract.song_df):
        print("Successfuly completed transform.py!")
    
        
    