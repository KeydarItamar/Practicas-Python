 # model de la clase product
from pydantic import BaseModel
from datetime import date

class Product(BaseModel):
    product_id: int
    name: str
    description : str
    company: str
    price: float
    units: int
    subcategory_id: int
  