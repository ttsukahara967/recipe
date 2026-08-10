from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict


class RecipeBase(BaseModel):
    title: str
    description: Optional[str] = None
    ingredients: Optional[str] = None
    steps: Optional[str] = None


class RecipeCreate(RecipeBase):
    pass


class RecipeUpdate(RecipeBase):
    pass


class RecipeOut(RecipeBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    created_at: datetime
    updated_at: datetime


class RecipeListOut(BaseModel):
    items: list[RecipeOut]
    total: int
    page: int
    page_size: int
