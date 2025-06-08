from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional

class UserBase(BaseModel):
    username: str
    email: str

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int

    class Config:
        from_attributes = True

class PurchaseBase(BaseModel):
    sku_name: str
    price: float
    quantity: int

class PurchaseCreate(PurchaseBase):
    user_id: int

class Purchase(PurchaseBase):
    id: int
    user_id: int
    datetime: datetime

    class Config:
        from_attributes = True 