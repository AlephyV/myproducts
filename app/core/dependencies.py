from app.db.session import get_db
from app.services.products_service import ProductService
from app.services.users_service import UserService
from fastapi import Depends, HTTPException, Request
from fastapi import Depends, HTTPException, status

def get_user_service(db=Depends(get_db)):
    return UserService(db)

def get_product_service(db=Depends(get_db)):
    return ProductService(db)

def get_current_user_from_service(
    request: Request,
    user_service: UserService = Depends(get_user_service)
):
    user_id = request.state.current_user
    if user_id is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not authenticated",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    current_user = user_service.get_user(user_id)
    current_user["id"] = current_user.pop("_id")
    
    if current_user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return current_user
