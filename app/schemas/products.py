from typing import Optional
from pydantic import BaseModel

class ProductBase(BaseModel):
    name: str
    brand: str
    price: float

class ProductCreate(ProductBase):
    pass

class ProductUpdate(BaseModel):
    name: Optional[str] = None
    brand: Optional[str] = None
    price: Optional[float] = None   

class Product(ProductBase):
    id: str
    owner: str
