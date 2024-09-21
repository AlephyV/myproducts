from pymongo import MongoClient

MONGO_USER = "root"
MONGO_PASSWORD = "example"
MONGO_HOST = "localhost"
MONGO_PORT = 27017
MONGO_DB = "products"

mongo_uri = f"mongodb://{MONGO_USER}:{MONGO_PASSWORD}@{MONGO_HOST}:{MONGO_PORT}/{MONGO_DB}?authSource=admin"

client = MongoClient(mongo_uri)
db = client[MONGO_DB]

def get_db():
    return db

