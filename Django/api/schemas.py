from pydantic import BaseModel

class ProductOut(BaseModel):

    title: str

    description: str

    created_at: str

    updated_at: str

    class Config:

        orm_mode = True

class ProductIn(BaseModel):

    title: str

    description: str