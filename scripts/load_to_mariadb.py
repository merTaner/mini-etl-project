from extract import extract_data
import pandas as pd
from sqlalchemy import create_engine
import time
from sqlalchemy.exc import OperationalError

def connect_with_retry(engine, max_retries=5, delay=5):
    for attempt in range(max_retries):
        try:
            return engine.connect()
        except OperationalError:
            if attempt == max_retries - 1:
                raise
            print(f"Connection attempt {attempt + 1} failed. Retrying in {delay} seconds...")
            time.sleep(delay)

def load_mariadb(engine, data):
    try:
        with connect_with_retry(engine) as connection:
            data.to_sql("movies", engine, if_exists="replace", index=False)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    engine = create_engine("mysql+pymysql://mert:44444444@172.80.0.30:3306/movies_db")
    data = extract_data("/app/data/raw/tmdb_5000_movies_and_credits.csv")
    load_mariadb(engine, data)
                 
