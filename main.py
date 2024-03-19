print("hello world")

import pymongo

def getConnection(db_id):
    print("Hello world")

def getCategory(category_id):
    try:
        # Connect to the database
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        db = client["mydatabase"]
        category_collection = db["category"]

        # Query the category collection for the specified category_id
        category = category_collection.find_one({"_id": category_id})

        return category
    except pymongo.errors.ConnectionFailure as e:
        print("Error connecting to the database:", e)
        return None
