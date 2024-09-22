from bson import ObjectId

from app.services.users_service import UserService

class ProductService:
    def __init__(self, db):
        self.db = db
        self.user_service = UserService(db)

    def create_product(self, product_data: dict, user_id: str):
        product_data['_id'] = str(ObjectId())
        product_data["owner"] = user_id
        
        self.db.products.insert_one(product_data)
        return product_data
        
    def read_product(self, product_id: str, user_id: str):
        product = self.db.products.find_one({"_id": product_id, "owner": user_id})
        if product:
            product["_id"] = str(product["_id"])
        return product
    
    def read_products(self, user_id: str):
        products = self.db.products.find({"owner": user_id})
        return [dict(product) for product in products]
    
    def update_product(self, product_id: str, product_data: dict, user_id: str):
        product_data = {k: v for k, v in product_data.items() if v is not None}
        updated_product = self.db.products.find_one_and_update(
            {"_id": product_id, "owner": user_id},
            {"$set": product_data},
            return_document=True
        )
        if updated_product:
            updated_product["_id"] = str(updated_product["_id"])
        return updated_product
    
    def delete_product(self, product_id: str, user_id: str):
        deleted_product = self.db.products.find_one_and_delete({"_id": product_id, "owner": user_id})
        if deleted_product:
            deleted_product["_id"] = str(deleted_product["_id"])
        return deleted_product