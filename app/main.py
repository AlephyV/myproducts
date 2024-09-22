from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from app.api.v1.endpoints import products, users
import logging
from starlette.middleware.base import BaseHTTPMiddleware

from app.core.auth import get_current_user
from app.core.loggin_config import setup_logging

setup_logging()

app = FastAPI()

app.include_router(products.router, prefix="/products", tags=["Products"])
app.include_router(users.router, prefix="/users", tags=["Users"])

@app.exception_handler(Exception)
async def general_exception_handler(request: Request, exc: Exception):
    logging.error(f"Unhandled exception: {exc}")
    return JSONResponse(
        status_code=500,
        content={"detail": "An internal server error occurred"},
    )

class CurrentUserMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        token = request.headers.get("Authorization")
        if token:
            try:
                token = token.replace("Bearer ", "")
                token_data = get_current_user(token)
                request.state.current_user = token_data.sub
            except HTTPException:
                request.state.current_user = None
        else:
            request.state.current_user = None

        response = await call_next(request)
        return response
    
app.add_middleware(CurrentUserMiddleware)