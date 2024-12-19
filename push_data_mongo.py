
from pymongo import MongoClient, ASCENDING
from key_data import *
import sys
import json

# Initialize MongoDB client
def get_db():
    try:
        client = MongoClient(MONGO_URI)
        client.admin.command('ping')
        print("got successful connection to MongoDB!")
        return client[DB_NAME]
    except Exception as e:
        print("error while connecting to MongoDB - %s"%(e))
        sys.exit(1)

def create_indexes(collection, indexes):
    final_indexes = []
    for index in indexes:
        final_indexes.append((index, ASCENDING))
    collection.create_index(final_indexes, unique=True)
    return collection

def get_users_collection(db):
    users_collection = db[USERS_COLLECTION]
    actual_indexes = ["email"]
    return create_indexes(users_collection, actual_indexes)

def get_exercises_collection(db):
    exercises_collection = db[EXERCISE_COLLECTION]
    actual_indexes = ['name', 'type', 'muscle', 'equipment', 'difficulty']
    return create_indexes(exercises_collection, actual_indexes)

db = get_db()
# users_collection = get_users_collection(db)
exercises_collection = get_exercises_collection(db)

def push_exercise_data_to_mongo():
    for file in ['beginner.json', 'intermediate.json', 'expert.json']:
        with open(file, 'r') as fin:
            collection_name = file.split('.')[0]
            data = json.load(fin)
            push_data = []
            for workout in data:
                if workout['instructions'] != "":
                    push_data.append(workout)
            for obj in push_data:
                print(obj['difficulty'], obj['name'])
                try:
                    exercises_collection.insert_one(obj)
                except Exception as e:
                    if 'DuplicateKeyError' in str(e):
                        print("data dupe found for %s"%(obj['name']))

if __name__ == "__main__":
    print("hello")
    push_exercise_data_to_mongo()