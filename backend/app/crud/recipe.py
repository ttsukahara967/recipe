from typing import Optional

from sqlalchemy import or_
from sqlalchemy.orm import Session

from app.models.recipe import Recipe
from app.schemas.recipe import RecipeCreate, RecipeUpdate


def get_recipes(db: Session, page: int = 1, page_size: int = 10, q: Optional[str] = None):
    query = db.query(Recipe)
    if q:
        pattern = f"%{q}%"
        query = query.filter(
            or_(
                Recipe.title.ilike(pattern),
                Recipe.description.ilike(pattern),
                Recipe.ingredients.ilike(pattern),
                Recipe.steps.ilike(pattern),
            )
        )
    total = query.count()
    items = (
        query.order_by(Recipe.id.desc())
        .offset((page - 1) * page_size)
        .limit(page_size)
        .all()
    )
    return items, total


def get_recipe(db: Session, recipe_id: int):
    return db.query(Recipe).filter(Recipe.id == recipe_id).first()


def create_recipe(db: Session, recipe: RecipeCreate):
    db_recipe = Recipe(**recipe.model_dump())
    db.add(db_recipe)
    db.commit()
    db.refresh(db_recipe)
    return db_recipe


def update_recipe(db: Session, recipe_id: int, recipe: RecipeUpdate):
    update_data = recipe.model_dump(exclude_unset=True)
    if not update_data:
        return None

    db.query(Recipe).filter(Recipe.id == recipe_id).update(
        update_data, synchronize_session=False
    )
    db.commit()

    return get_recipe(db, recipe_id)


def delete_recipe(db: Session, recipe_id: int):
    db_recipe = get_recipe(db, recipe_id)
    if db_recipe is None:
        return None
    db.delete(db_recipe)
    db.commit()
    return db_recipe
