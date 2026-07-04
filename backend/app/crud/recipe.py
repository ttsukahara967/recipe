from sqlalchemy.orm import Session

from app.models.recipe import Recipe
from app.schemas.recipe import RecipeCreate, RecipeUpdate


def get_recipes(db: Session):
    return db.query(Recipe).order_by(Recipe.id.desc()).all()


def get_recipe(db: Session, recipe_id: int):
    return db.query(Recipe).filter(Recipe.id == recipe_id).first()


def create_recipe(db: Session, recipe: RecipeCreate):
    db_recipe = Recipe(**recipe.model_dump())
    db.add(db_recipe)
    db.commit()
    db.refresh(db_recipe)
    return db_recipe


def update_recipe(db: Session, recipe_id: int, recipe: RecipeUpdate):
    db_recipe = get_recipe(db, recipe_id)
    if db_recipe is None:
        return None
    for key, value in recipe.model_dump().items():
        setattr(db_recipe, key, value)
    db.commit()
    db.refresh(db_recipe)
    return db_recipe


def delete_recipe(db: Session, recipe_id: int):
    db_recipe = get_recipe(db, recipe_id)
    if db_recipe is None:
        return None
    db.delete(db_recipe)
    db.commit()
    return db_recipe
