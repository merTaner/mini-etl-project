from pymongo import MongoClient
from transfrom import main

def load_to_mongo(data):
    try:
        client = MongoClient("mongodb://mert:4444@mongodb-container:27017/")

        #create db and collection
        db = client["movies_db"]
        movie_collection = db["movies"]

        for _, row in data.iterrows():
            # change to collection name per each itaration
            collection_name = row["original_title"]
            sanitized_name = ''.join(e for e in collection_name if e.isalnum() or e.isspace()).replace('.', ' ')

            collection = movie_collection[sanitized_name]

            # change row format to json
            json_data = row.to_dict()
            collection.insert_one(json_data)

    except Exception as e:
        print(f"Error: {e}")


if __name__ == '__main__':
    transformed_data = main()
    if transformed_data is not None:
        load_to_mongo(transformed_data)

