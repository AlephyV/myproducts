from pydantic import BaseModel

class Product(BaseModel):
    id: str
    name: str
    brand: str
    price: float
    owner: str
    