
from pydantic import BaseModel

class Product(BaseModel):
    
    id: str
    sku: str
    external_id: str
    name: str
    description: str
    image: List[str]
    type: str
    amount: int
    currency: str
    availability: bool