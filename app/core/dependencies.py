from app.db.session import get_db
from app.services.products_service import ProductService
from app.services.users_service import UserService
from fastapi import Depends

def get_user_service(db=Depends(get_db)):
    return UserService(db)

def get_product_service(db=Depends(get_db)):
    return ProductService(db)