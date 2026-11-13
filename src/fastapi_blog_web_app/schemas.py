from pydantic import BaseModel, ConfigDict, Field, EmailStr
from typing import Annotated



class UserBase(BaseModel):
    username: Annotated[str, Field(min_length=1, max_length=30)]
    email: Annotated[EmailStr, Field(max_length=50)]
    
class UserCreate(UserBase):
    pass

class UserResponse(UserBase):
    model_config=ConfigDict(from_attributes=True)

    id: int
    image_file: str | None
    image_path: str



class PostBase(BaseModel):
    title: Annotated[str, Field(min_length=1, max_length=100)]
    content: Annotated[str, Field(min_length=1)]
    author: Annotated[str, Field(min_length=1, max_length=30)]

class PostCreate(PostBase):
    pass

class PostResponse(PostBase):
    model_config=ConfigDict(from_attributes=True)

    id: int
    date_posted: str                   