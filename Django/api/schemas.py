from pydantic import BaseModel, validator
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

    title: str

    description: str