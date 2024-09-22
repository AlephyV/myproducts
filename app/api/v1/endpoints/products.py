from fastapi import APIRouter, Depends, HTTPException
from pymongo.errors import DuplicateKeyError

from app.schemas.products import Product, ProductCreate, ProductUpdate
from app.core.dependencies import get_current_user_from_service, get_product_service
from app.schemas.users import User
from app.services.products_service import ProductService

router = APIRouter()

@router.post("/", response_model=Product)
async def create_product(product: ProductCreate, product_service: ProductService = Depends(get_product_service), current_user: User = Depends(get_current_user_from_service)):
    try:
        created_product = product_service.create_product(product.model_dump(), current_user["id"])
        created_product["id"] = created_product.pop("_id")
        return Product(**created_product)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except DuplicateKeyError:
        raise HTTPException(status_code=400, detail="Product already exists")

@router.get("/{product_id}", response_model=Product)
async def read_product(product_id: str, product_service: ProductService = Depends(get_product_service), current_user: User = Depends(get_current_user_from_service)):
    product = product_service.read_product(product_id, current_user["id"])
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    product["id"] = product.pop("_id")
    return Product(**product)

@router.get("/", response_model=list[Product])
async def read_products(product_service: ProductService = Depends(get_product_service), current_user: User = Depends(get_current_user_from_service)):
    products = product_service.read_products(current_user["id"])
    for product in products:
        product["id"] = product.pop("_id")
    return [Product(**product) for product in products]

@router.put("/{product_id}", response_model=Product)
async def update_product(product_id: str, product: ProductUpdate, product_service: ProductService = Depends(get_product_service), current_user: User = Depends(get_current_user_from_service)):
    updated_product = product_service.update_product(product_id, product.model_dump(), current_user["id"])
    if updated_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    updated_product["id"] = updated_product.pop("_id")
    return Product(**updated_product)

@router.delete("/{product_id}", response_model=Product)
async def delete_product(product_id: str, product_service: ProductService = Depends(get_product_service), current_user: User = Depends(get_current_user_from_service)):
    deleted_product = product_service.delete_product(product_id, current_user["id"])
    if deleted_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    deleted_product["id"] = deleted_product.pop("_id")
    return Product(**deleted_product)