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

- `GET /api/recipes/` list
- `GET /api/recipes/{id}` get one
- `POST /api/recipes/` create
- `PUT /api/recipes/{id}` update
- `DELETE /api/recipes/{id}` delete

This is still just a skeleton — auth, image upload, and categorization are not implemented yet.
