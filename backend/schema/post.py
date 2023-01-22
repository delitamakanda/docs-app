from typing import Optional
from pydantic import BaseModel

class PostBase(BaseModel):
    title: str
    body: str

    class Config:
        orm_mode = True

class PostCreate(PostBase):
    pass

class PostUpdate(PostBase):
    pass


class PostInDBBase(PostBase):
    id: int
    title: str
    owner_id: int

    class Config:
        orm_mode = True

class Post(PostInDBBase):
    pass

class PostInDB(PostInDBBase):
    pass