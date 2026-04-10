---
description: "Use when writing or editing test files. Covers pytest patterns, async testing, fixtures, and test naming for this FastAPI project."
applyTo: "tests/**/*.py"
---
# Testing Conventions

## Framework

- Use `pytest` with `pytest-asyncio`
- Use `httpx.AsyncClient` for API testing
- Test files: `tests/test_<module>.py`

## Structure

```python
import pytest
from httpx import ASGITransport, AsyncClient
from app.main import app

@pytest.mark.asyncio
async def test_create_entity():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
        response = await client.post("/entity", json={...})
    assert response.status_code == 201
```

## Naming

- Test functions: `test_<action>_<entity>[_<scenario>]`
- Examples: `test_create_user`, `test_get_user_not_found`, `test_list_products_empty`

## Coverage

Each module must test:
1. Create entity (201)
2. Get entity by ID (200)
3. Get entity not found (404)
4. List all entities (200)
5. Update entity (200)
6. Delete entity (200)

## Assertions

- Always assert `status_code` first
- Then assert response body structure
- Use `response.json()` to inspect body
