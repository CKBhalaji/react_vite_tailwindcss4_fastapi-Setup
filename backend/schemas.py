# backend/schemas.py
from pydantic import BaseModel, ConfigDict
from typing import Optional

# Pydantic model for creating an Item (request body)
class ItemCreate(BaseModel):
    name: str
    description: Optional[str] = None

# Pydantic model for an Item (response body)
class Item(BaseModel):
    id: int
    name: str
    description: Optional[str] = None

    # This 'Config' class tells Pydantic to work with SQLAlchemy models
    # It allows Pydantic to read data from ORM objects.
    model_config = ConfigDict(from_attributes=True) # For Pydantic v2+
    # For Pydantic v1, it would be: class Config: orm_mode = True