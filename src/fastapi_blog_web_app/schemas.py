from pydantic import BaseModel, ConfigDict, Field
from typing import Annotated



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