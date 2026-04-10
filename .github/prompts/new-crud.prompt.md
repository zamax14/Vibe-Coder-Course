---
description: "Generate a complete CRUD module for a new entity following project conventions. Provide the entity name, fields, and relationships."
agent: "agent"
argument-hint: "Entity name, fields and relationships (e.g. 'Category with name:str, description:str|None')"
---
Generate a complete CRUD module for the entity described below. Follow the project's modular architecture strictly.

## Requirements

Create all 7 files under `app/<entity_name>/`:

1. **`__init__.py`** — Empty file
2. **`constants.py`** — `ENTITY_NAME` and `MESSAGES` dict with keys: `not_found`, `created`, `updated`, `deleted`, `already_exists`
3. **`exceptions.py`** — `<Entity>NotFoundException` and `<Entity>AlreadyExistsException` (if applicable)
4. **`models.py`** — SQLAlchemy 2.0 model with `Mapped` + `mapped_column`, always include `id`, `created_at`, `updated_at`
5. **`schemas.py`** — Pydantic v2 schemas: `<Entity>Create`, `<Entity>Update` (all optional), `<Entity>Response` (with `ConfigDict(from_attributes=True)`)
6. **`service.py`** — Async functions: `get_all`, `get_by_id`, `create`, `update`, `delete` using `AsyncSession`
7. **`routes.py`** — `APIRouter` with prefix and tags, standard 5 CRUD endpoints

Then register the router in [app/main.py](app/main.py) by adding the import and `app.include_router()`.

## Reference

Follow the exact patterns from [users module](app/users/) as reference.
