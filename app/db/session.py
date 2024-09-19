from contextlib import contextmanager
from pymongo import MongoClient

DATABASE_URL = "mongodb://localhost:27017/"
DATABASE_NAME = "products"

client = MongoClient(DATABASE_URL)
db = client[DATABASE_NAME]

def get_db():
    return db