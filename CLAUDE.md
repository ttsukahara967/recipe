# CLAUDE.md

Guidance for working in this repository.

## Overview

A recipe management system. Still at the skeleton stage — only recipe CRUD is implemented so far.

- Frontend: React (Vite) — `frontend/`
- Backend: FastAPI — `backend/`
- DB: MySQL — managed via Docker Compose
- Environment: Docker Compose (`docker-compose.yml`)

## Running

```bash
docker compose up --build
```

- Frontend: http://localhost:5173
- Backend API: http://localhost:8000
- API docs (Swagger): http://localhost:8000/docs

To run services individually:

```bash
# backend
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload

# frontend
cd frontend
npm install
npm run dev
```

## Directory structure

```
backend/app/
├── main.py          # App startup, CORS config, auto table creation
├── db/database.py   # SQLAlchemy engine & session
├── models/          # SQLAlchemy models (table definitions)
├── schemas/          # Pydantic schemas (request/response)
├── crud/             # DB operation functions
└── routers/          # API endpoints (under /api/)
backend/tests/        # pytest suite (see Testing below)

frontend/src/
├── App.jsx           # Route definitions (react-router-dom)
├── api.js            # Backend API calls (fetch wrapper)
├── main.jsx
└── pages/
    ├── RecipeList.jsx  # Public page: search + paginated browsing (no auth)
    └── AdminPage.jsx   # /admin: create, edit, delete (no auth)

db-init/               # SQL run by the MySQL container on first init
```

When adding a new resource, create files in this order: `models/` → `schemas/` → `crud/` → `routers/`, then register it with `include_router` in `main.py`.

## Testing

Backend tests live in `backend/tests/` and run against a separate `recipe_test_db` database rather than the real `recipe_db` (see `backend/tests/conftest.py` and `db-init/01_test_db.sql`). Each test run creates the tables, and fixtures seed/clean rows per test; tables are dropped again at the end of the session.

```bash
docker compose exec backend pip install -r requirements-dev.txt
docker compose exec backend pytest
```

`recipe_test_db` is created automatically by `db-init/01_test_db.sql` when the `db` container initializes its data volume for the first time. If the DB volume already existed before this script was added, apply it manually once: `docker compose exec -T db mysql -uroot -proot_pass < db-init/01_test_db.sql`.

## Conventions & notes

- Backend DB connection is configured via the `DATABASE_URL` env var (defaults to the `db` service in Docker Compose).
- Frontend API base URL is configured via the `VITE_API_BASE_URL` env var (defaults to `http://localhost:8000`).
- Auth, image upload, and category features are not implemented yet. The `/admin` page is not access-controlled — it's reachable by anyone who knows the URL.
