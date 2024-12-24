from pydantic import BaseModel, validator, root_validator
from typing import Optional
from datetime import datetime

class ProductOut(BaseModel):

    id: int

    title: str

    description: str

    created_at: str

    updated_at: str

    class Config:

        orm_mode = True
        from_attributes = True


    @validator("created_at", pre=True)
    def convert_created_at(cls, v):
        if isinstance(v, datetime):
            return v.isoformat()
        return v

    @validator("updated_at", pre=True)
    def convert_updated_at(cls, v):
        if isinstance(v, datetime):
            return v.isoformat()
        return v


class ProductIn(BaseModel):

    title: Optional[str] = None

    description: Optional[str] = None

    @root_validator(pre=True)
    def check_at_least_one_field(cls, values):
        title = values.get('title')
        description = values.get('description')
        
        if not title and not description:
            raise ValueError('At least one field (title or description) must be provided.')
        
        return values