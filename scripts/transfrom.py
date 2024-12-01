import pandas as pd
from sqlalchemy import create_engine, text

def transform_data(df):
    # pull data from mariadb 
    # applying tranforms to these data

    # drop unnecessary colums
    df.drop(["genres", "homepage", "keywords", "original_language", 
             "production_companies", "production_countries", 
             "spoken_languages", "status"], axis=1, inplace=True)

    # drop to null values
    df.dropna(inplace=True)
    
    # type changing for same colums
    df['release_date'] = pd.to_datetime(df['release_date'], errors='coerce')
    df['budget'] = pd.to_numeric(df['budget'], errors='coerce')
    df['revenue'] = pd.to_numeric(df['revenue'], errors='coerce')
    
    # we'll filtering then 2014 years because we want show last 10 years data
    df = df[df['release_date'].dt.year > 2014]

    # we'll chose/filtering budget have greater then 50mil
    df = df[df['budget'] > 50000000]

    # calculate profit with using revenue and budget columns
    df["profit"] = df["revenue"] - df["budget"]

    # Making a categorical classification with the 'runtime' column
    bins = [0, 90, 150, float('inf')]
    labels = ['Short', 'Medium', 'Long']
    df['movie_length'] = pd.cut(df['runtime'], bins=bins, labels=labels, right=False)

    #df.to_csv("out.csv", index=False)
    return df
    
def main():
    engine = create_engine("mysql+pymysql://mert:4444@localhost:3306/movies_db")
    
    try:
        with engine.connect() as connection:
            data = pd.read_sql(text("SELECT * FROM movies;"), con=connection)
            transformed_data = transform_data(df=data)
            return transformed_data
    except Exception as e:
        print(f"Error : {e}")
        return None

if __name__ == '__main__':
    main()

    


