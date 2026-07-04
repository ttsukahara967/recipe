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

frontend/src/
├── App.jsx           # Recipe list / create / delete screen
├── api.js            # Backend API calls (fetch wrapper)
└── main.jsx
```

When adding a new resource, create files in this order: `models/` → `schemas/` → `crud/` → `routers/`, then register it with `include_router` in `main.py`.

## Conventions & notes

- Backend DB connection is configured via the `DATABASE_URL` env var (defaults to the `db` service in Docker Compose).
- Frontend API base URL is configured via the `VITE_API_BASE_URL` env var (defaults to `http://localhost:8000`).
- Auth, image upload, and category features are not implemented yet.
