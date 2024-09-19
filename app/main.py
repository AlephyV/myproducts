from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from app.api.v1.endpoints import users
import logging

from app.core.loggin_config import setup_logging

setup_logging()

app = FastAPI()

#app.include_router(products.router, prefix="/products", tags=["Products"])
app.include_router(users.router, prefix="/users", tags=["Users"])

@app.exception_handler(Exception)
async def general_exception_handler(request: Request, exc: Exception):
    logging.error(f"Unhandled exception: {exc}")
    return JSONResponse(
        status_code=500,
        content={"detail": "An internal server error occurred"},
    )
