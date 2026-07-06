# Recipe Management System (Skeleton)

This is a proof-of-concept project built with Claude Code, used to experiment with and evaluate its capabilities.

- Frontend: React (Vite)
- Backend: FastAPI
- DB: MySQL
- Environment: Docker Compose

## Running

```bash
docker compose up --build
```

- Frontend: http://localhost:5173
- Backend API: http://localhost:8000
- API docs: http://localhost:8000/docs

## Structure

```
recipe/
├── backend/        # FastAPI
│   └── app/
│       ├── main.py
│       ├── db/         # DB connection
│       ├── models/     # SQLAlchemy models
│       ├── schemas/    # Pydantic schemas
│       ├── crud/       # DB operations
│       └── routers/    # API endpoints
├── frontend/       # React (Vite)
│   └── src/
├── docker-compose.yml
```

## Implemented API (recipe CRUD)

- `GET /api/recipes/` list (paginated, supports `q` text search)
- `GET /api/recipes/{id}` get one
- `POST /api/recipes/` create
- `PUT /api/recipes/{id}` update
- `DELETE /api/recipes/{id}` delete

## Testing

Tests run against a dedicated `recipe_test_db` database (created automatically alongside `recipe_db` when the `db` container starts, see `db-init/01_test_db.sql`). Test setup creates the tables, seeds fixture data per test, and drops the tables again afterward — the real `recipe_db` is never touched.

```bash
docker compose exec backend pip install -r requirements-dev.txt
docker compose exec backend pytest
```

This is still just a skeleton — auth, image upload, and categorization are not implemented yet.
