import os

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.db.database import Base, get_db
from app.main import app
from app.models.recipe import Recipe

TEST_DATABASE_URL = os.getenv(
    "TEST_DATABASE_URL",
    "mysql+pymysql://recipe_user:recipe_pass@db:3306/recipe_test_db",
)

engine = create_engine(TEST_DATABASE_URL, pool_pre_ping=True)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def _override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = _override_get_db


@pytest.fixture(scope="session", autouse=True)
def test_database():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)


@pytest.fixture(autouse=True)
def clean_tables():
    db = TestingSessionLocal()
    db.query(Recipe).delete()
    db.commit()
    db.close()
    yield


@pytest.fixture
def seed_recipes():
    db = TestingSessionLocal()
    recipes = [
        Recipe(
            title="カレーライス",
            description="定番の家庭料理",
            ingredients="じゃがいも, 玉ねぎ, にんじん, カレールー",
            steps="具材を切って煮込み、ルーを溶かす",
        ),
        Recipe(
            title="肉じゃが",
            description="和食の定番",
            ingredients="じゃがいも, 牛肉, 玉ねぎ",
            steps="炒めて煮込む",
        ),
        Recipe(
            title="味噌汁",
            description="毎日の一杯",
            ingredients="味噌, 豆腐, わかめ",
            steps="出汁を取り、具材を入れて味噌を溶く",
        ),
    ]
    db.add_all(recipes)
    db.commit()
    ids = [r.id for r in recipes]
    db.close()
    return ids


@pytest.fixture
def client():
    return TestClient(app)
