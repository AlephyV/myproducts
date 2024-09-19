# from fastapi import APIRouter, HTTPException, Depends
# from sqlalchemy.orm import Session
# from typing import List
# from app import models, schemas, crud
# from app.database import get_db

# router = APIRouter()

# @router.post("/", response_model=schemas.Product)
# def create_product(product: schemas.ProductCreate, db: Session = Depends(get_db)):
#     db_product = crud.get_product_by_name(db, name=product.name)
#     if db_product:
#         raise HTTPException(status_code=400, detail="Product already registered")
#     return crud.create_product(db=db, product=product)

# @router.get("/", response_model=List[schemas.Product])
# def read_products(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
#     products = crud.get_products(db, skip=skip, limit=limit)
#     return products

# @router.get("/{product_id}", response_model=schemas.Product)
# def read_product(product_id: int, db: Session = Depends(get_db)):
#     db_product = crud.get_product(db, product_id=product_id)
#     if db_product is None:
#         raise HTTPException(status_code=404, detail="Product not found")
#     return db_product

# @router.put("/{product_id}", response_model=schemas.Product)
# def update_product(product_id: int, product: schemas.ProductUpdate, db: Session = Depends(get_db)):
#     db_product = crud.get_product(db, product_id=product_id)
#     if db_product is None:
#         raise HTTPException(status_code=404, detail="Product not found")
#     return crud.update_product(db=db, product=product, product_id=product_id)

# @router.delete("/{product_id}", response_model=schemas.Product)
# def delete_product(product_id: int, db: Session = Depends(get_db)):
#     db_product = crud.get_product(db, product_id=product_id)
#     if db_product is None:
#         raise HTTPException(status_code=404, detail="Product not found")
#     return crud.delete_product(db=db, product_id=product_id)