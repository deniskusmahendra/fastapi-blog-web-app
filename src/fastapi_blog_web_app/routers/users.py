from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

import fastapi_blog_web_app.models as models
from fastapi_blog_web_app.database import get_db
from fastapi_blog_web_app.schemas import PostResponse, UserCreate, UserResponse, UserUpdate