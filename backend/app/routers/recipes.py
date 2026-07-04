from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.crud import recipe as crud
from app.db.database import get_db
from app.schemas.recipe import RecipeCreate, RecipeOut, RecipeUpdate

router = APIRouter(prefix="/api/recipes", tags=["recipes"])


@router.get("/", response_model=list[RecipeOut])
def list_recipes(db: Session = Depends(get_db)):
    return crud.get_recipes(db)


@router.get("/{recipe_id}", response_model=RecipeOut)
def read_recipe(recipe_id: int, db: Session = Depends(get_db)):
    db_recipe = crud.get_recipe(db, recipe_id)
    if db_recipe is None:
        raise HTTPException(status_code=404, detail="Recipe not found")
    return db_recipe


@router.post("/", response_model=RecipeOut, status_code=201)
def create_recipe(recipe: RecipeCreate, db: Session = Depends(get_db)):
    return crud.create_recipe(db, recipe)


@router.put("/{recipe_id}", response_model=RecipeOut)
def update_recipe(recipe_id: int, recipe: RecipeUpdate, db: Session = Depends(get_db)):
    db_recipe = crud.update_recipe(db, recipe_id, recipe)
    if db_recipe is None:
        raise HTTPException(status_code=404, detail="Recipe not found")
    return db_recipe


@router.delete("/{recipe_id}", status_code=204)
def delete_recipe(recipe_id: int, db: Session = Depends(get_db)):
    db_recipe = crud.delete_recipe(db, recipe_id)
    if db_recipe is None:
        raise HTTPException(status_code=404, detail="Recipe not found")
