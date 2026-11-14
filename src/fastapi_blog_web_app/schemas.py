from pydantic import BaseModel, ConfigDict, Field, EmailStr
from typing import Annotated
from datetime import datetime



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

class UserUpdate(BaseModel):
    username: Annotated[str | None, Field(default=None, min_length=1, max_length=50)]
    email: Annotated[EmailStr | None, Field(default=None, max_length=120)]
    image_file: Annotated[str | None, Field(default=None, min_length=1, max_length=200)]



class PostBase(BaseModel):
    title: Annotated[str, Field(min_length=1, max_length=100)]
    content: Annotated[str, Field(min_length=1)]

class PostCreate(PostBase):
    user_id: int   # TEMPORARY

class PostUpdate(BaseModel):
    title: Annotated[str | None, Field(default=None, min_length=1, max_length=100)]
    content: Annotated[str | None, Field(default=None, min_length=1)]

class PostResponse(PostBase):
    model_config=ConfigDict(from_attributes=True)

    id: int
    user_id: int
    date_posted: datetime
    author: UserResponse                   