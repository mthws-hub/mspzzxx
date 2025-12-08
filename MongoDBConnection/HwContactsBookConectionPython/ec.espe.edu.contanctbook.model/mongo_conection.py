from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

def get_db_collection():
    uri = "mongodb+srv://Mathews:Mathews2007@cluster0.6l9ibfh.mongodb.net/"
    try:
        client = MongoClient(uri)
        client.admin.command('ping')
        print("Successful Connection")
        db = client['ContactBook']
        return db['Contacts']
    except ConnectionFailure:
        print("Error")
        return None