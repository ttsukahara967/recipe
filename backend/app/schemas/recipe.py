from datetime import datetime

from pydantic import BaseModel, ConfigDict


class RecipeBase(BaseModel):
    title: str
    description: str | None = None
    ingredients: str | None = None
    steps: str | None = None


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
