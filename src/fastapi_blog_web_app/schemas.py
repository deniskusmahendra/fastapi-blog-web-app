from datetime import datetime
from typing import Annotated

from pydantic import BaseModel, ConfigDict, EmailStr, Field


class UserBase(BaseModel):
    username: Annotated[str, Field(min_length=1, max_length=30)]
    email: Annotated[EmailStr, Field(max_length=50)]


class UserCreate(UserBase):
    password: Annotated[str, Field(min_lenghth=8)]


class UserPublic(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    username: str
    image_file: str | None
    image_path: str


class UserPrivate(UserPublic):
    email: EmailStr


class UserUpdate(BaseModel):
    username: Annotated[str | None, Field(default=None, min_length=1, max_length=50)]
    email: Annotated[EmailStr | None, Field(default=None, max_length=120)]
    

class Token(BaseModel):
    access_token: str
    token_type: str


# ======================================================================================


class PostBase(BaseModel):
    title: Annotated[str, Field(min_length=1, max_length=100)]
    content: Annotated[str, Field(min_length=1)]


class PostCreate(PostBase):
    pass


class PostUpdate(BaseModel):
    title: Annotated[str | None, Field(default=None, min_length=1, max_length=100)]
    content: Annotated[str | None, Field(default=None, min_length=1)]


class PostResponse(PostBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    user_id: int
    date_posted: datetime
    author: UserPublic


class PaginatedPostResponse(BaseModel):
    posts: list[PostResponse]
    total: int
    skip: int
    limit: int
    has_more: bool