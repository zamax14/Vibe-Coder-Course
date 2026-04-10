# Project Guidelines — Vibe Engineer API

## Architecture

This is a FastAPI REST API with PostgreSQL. The codebase follows a **modular architecture** where each domain entity lives in its own package under `app/`.

### Module Structure

Every module (entity) follows this exact structure:

```
app/<module_name>/
├── __init__.py      # Empty
├── models.py        # SQLAlchemy ORM models
├── schemas.py       # Pydantic schemas (Create, Update, Response)
├── routes.py        # FastAPI router with endpoints
├── service.py       # Business logic and DB operations
├── constants.py     # Response messages and fixed values
└── exceptions.py    # Custom HTTP exceptions
```

### Key Files

- `app/main.py` — App factory and router registration
- `app/database.py` — Async SQLAlchemy engine and session
- `app/config.py` — Pydantic Settings for environment variables

## Code Style

- Language: Python 3.11+
- Code and variable names: **English**
- Type hints on all function signatures
- Async/await for all DB operations
- Use `AsyncSession` from SQLAlchemy for database access
- Pydantic v2 with `model_config = ConfigDict(from_attributes=True)`

## Conventions

### Routes

- All routers use `APIRouter` with a `prefix` and `tags`
- Standard CRUD endpoints per module: `GET /`, `GET /{id}`, `POST /`, `PUT /{id}`, `DELETE /{id}`
- Return Pydantic response schemas, never raw ORM objects
- Use `status_code` parameter on route decorators

### Services

- One function per CRUD operation: `get_all`, `get_by_id`, `create`, `update`, `delete`
- Accept `AsyncSession` as first parameter via `Depends(get_session)`
- Raise exceptions from the module's `exceptions.py`, never use `HTTPException` directly in services

### Constants

- Define `MESSAGES` dict with keys: `not_found`, `created`, `updated`, `deleted`, `already_exists`
- Use f-strings with the entity name for consistency

### Exceptions

- Define `NotFoundException` and `AlreadyExistsException` per module
- Inherit from a base `raise HTTPException` pattern with status codes from `constants.py`

### Models

- All models inherit from `Base` (from `app/database.py`)
- Use `Mapped` and `mapped_column` (SQLAlchemy 2.0 style)
- Always include `id`, `created_at`, `updated_at` columns

### Schemas

- Three schemas per entity: `<Entity>Create`, `<Entity>Update`, `<Entity>Response`
- `Update` schema has all fields optional
- `Response` schema includes `id`, `created_at`, `updated_at`

## Build and Test

```bash
# Install dependencies
pip install -r requirements.txt

# Run development server
uvicorn app.main:app --reload

# Run tests
pytest tests/ -v

# Docker
docker compose up --build
```

## Error Handling

- Use module-level custom exceptions, not generic HTTPException
- All error responses follow: `{"detail": "message"}`
- 404 for not found, 409 for conflicts, 422 for validation (automatic by FastAPI)
