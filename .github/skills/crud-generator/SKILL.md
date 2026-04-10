---
name: crud-generator
description: "Generate a full CRUD module for a FastAPI entity. Use when adding a new entity, creating API endpoints, or scaffolding a new module. Includes model, schemas, routes, service, constants, exceptions, and tests."
argument-hint: "Entity name and fields (e.g., 'Category: name str, description str optional')"
---

# CRUD Module Generator

## When to Use

- Adding a new entity/resource to the API
- Scaffolding a complete CRUD module
- Need all 7 files + tests + router registration

## Procedure

### Step 1: Gather Information

From the user input, extract:
- **Entity name** (singular, PascalCase for class, snake_case for module)
- **Fields** with types and constraints
- **Unique field** (for already-exists check) — if any
- **Foreign keys** — if any

### Step 2: Create Module Files

Create `app/<entity_snake>/` with these 7 files following the templates in [references](./references/templates.md):

1. `__init__.py` — Empty
2. `constants.py` — Entity messages
3. `exceptions.py` — NotFoundException + AlreadyExistsException
4. `models.py` — SQLAlchemy 2.0 model
5. `schemas.py` — Pydantic v2 Create/Update/Response
6. `service.py` — Async CRUD functions
7. `routes.py` — APIRouter with 5 endpoints

### Step 3: Register Router

Add to `app/main.py`:
```python
from app.<entity_snake>.routes import router as <entity_snake>_router
app.include_router(<entity_snake>_router)
```

### Step 4: Create Tests

Create `tests/test_<entity_snake>.py` with 6 standard tests following [test patterns](./references/test-patterns.md).

### Step 5: Verify

- Check for import errors
- Ensure all files follow project conventions
- Confirm router is registered

## Reference Files

- [Module templates](./references/templates.md) — Code templates for each file
- [Test patterns](./references/test-patterns.md) — Standard test patterns
