# import our get connection function
from utils import dbconfig
from pymongo import MongoClient
from json import dumps
from bson.objectid import ObjectId


# pull a specific deck from the database
def get_deck(user_id, deck_name):
    # create result variable
    result = None
    try:
        connection = dbconfig.get_mongo_connection()
        database = connection["spell-binder"]
        collection = database["decks"]
        query = {"user_id": user_id, "deck_name": deck_name}
        result = collection.find_one(query)
        result = dumps(result)
    finally:
        # close our database connection
        connection.close()
        # return the result
        return result


# insert a new deck into the database
def insert_deck(new_deck_json):
    # create result variable
    result = None
    try:
        connection = dbconfig.get_mongo_connection()
        database = connection["spell-binder"]
        collection = database["decks"]
        result = collection.insert_one(new_deck_json)
    finally:
        # close our database connection
        connection.close()
        # return the result
        return "New deck ID = " + str(result.inserted_id)


# replace an existing deck in the database
def replace_deck(deck_id, new_deck_json):
    # create result variable
    result = None
    try:
        connection = dbconfig.get_mongo_connection()
        database = connection["spell-binder"]
        collection = database["decks"]
        query_filter = {"_id": ObjectId(deck_id)}
        replace_document = new_deck_json
        result = collection.replace_one(query_filter, replace_document)
    finally:
        # close our database connection
        connection.close()
        # return the result
        return "Number of decks modified = " + str(result.modified_count)

