from fastapi import APIRouter, Depends

from app.schemas.users import Token, User, UserCreate, UserLogin
from app.core.dependencies import get_current_user_from_service, get_user_service
from app.services.users_service import UserService
from fastapi import HTTPException, status

router = APIRouter()

@router.post("/register", response_model=User)
async def register_user(user: UserCreate, user_service: UserService = Depends(get_user_service)):
    user = user_service.create_user(user.model_dump())
    user["id"] = user.pop("_id")
    user_response = User(**user)
    return user_response

@router.post("/token", response_model=Token)
async def login_user(user: UserLogin, user_service: UserService = Depends(get_user_service)):
    authenticated_user = user_service.authenticate_user(user.email, user.password)
    if not authenticated_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    return authenticated_user

@router.get("/me", response_model=User)
async def read_users_me(current_user: User = Depends(get_current_user_from_service)):
    return current_user