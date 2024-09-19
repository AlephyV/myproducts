import bcrypt
from bson.objectid import ObjectId

from app.core.auth import create_access_token

class UserService:
    def __init__(self, db):
        self.db = db

    def create_user(self, user_data: dict):
        user_data["_id"] = str(ObjectId())
        user_data["password"] = bcrypt.hashpw(user_data["password"].encode('utf-8'), bcrypt.gensalt())
        self.db.users.insert_one(user_data)
        return user_data

    def get_user(self, user_id: str):
        user = self.db.users.find_one({"_id": user_id})
        if user:
            user["_id"] = str(user["_id"])
        return user
    
    def authenticate_user(self, email: str, password: str):
        user = self.db.users.find_one({"email": email})
        if user:
            stored_password = user["password"]
            if isinstance(stored_password, str):
                stored_password = stored_password.encode('utf-8')
            if bcrypt.checkpw(password.encode('utf-8'), stored_password):
                user["_id"] = str(user["_id"])
                access_token = create_access_token(data={"sub": user["_id"]})
                return {"access_token": access_token, "token_type": "bearer"}
        return None