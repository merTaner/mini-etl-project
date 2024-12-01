from scripts.extract import extract_data
import pandas as pd
from sqlalchemy import create_engine


def load_mariadb(engine, data):
    try:
        # Upload data to the MariaDB table
        with engine.connect() as connection:
            # Check if the table exists; if not, create it
            data.to_sql("movies", engine, if_exists="replace", index=False)
    except Exception as e:
        print(f"Error : {e}")


if __name__ == "__main__":
    # Connection parameters
    engine = create_engine("mysql+pymysql://mert:4444@localhost:3306/movies_db")
    data = extract_data("C:/Users/mertt/mini-data-pipeline-project/data/raw/tmdb_5000_movies_and_credits.csv")
    
    load_mariadb(engine, data)