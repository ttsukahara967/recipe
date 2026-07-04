from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.db.database import Base, engine
from app.models import recipe as recipe_model  # noqa: F401  (registers model)
from app.routers import recipes

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Recipe Management API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(recipes.router)


@app.get("/api/health")
def health_check():
    return {"status": "ok"}
