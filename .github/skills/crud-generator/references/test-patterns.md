# Test Patterns

Standard test patterns for CRUD modules. Replace `<entity>` with snake_case name, `<Entity>` with PascalCase.

## File Structure

Create `tests/test_<entity>.py`:

```python
import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_create_<entity>(client: AsyncClient):
    response = await client.post("/<entities>/", json={
        # Required fields for creation
    })
    assert response.status_code == 201
    data = response.json()
    # Assert key fields match input


@pytest.mark.asyncio
async def test_list_<entities>(client: AsyncClient):
    # Create one first
    await client.post("/<entities>/", json={...})
    response = await client.get("/<entities>/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


@pytest.mark.asyncio
async def test_get_<entity>(client: AsyncClient):
    create = await client.post("/<entities>/", json={...})
    entity_id = create.json()["id"]
    response = await client.get(f"/<entities>/{entity_id}")
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_get_<entity>_not_found(client: AsyncClient):
    response = await client.get("/<entities>/9999")
    assert response.status_code == 404


@pytest.mark.asyncio
async def test_update_<entity>(client: AsyncClient):
    create = await client.post("/<entities>/", json={...})
    entity_id = create.json()["id"]
    response = await client.put(f"/<entities>/{entity_id}", json={
        # Fields to update
    })
    assert response.status_code == 200
    # Assert updated values


@pytest.mark.asyncio
async def test_delete_<entity>(client: AsyncClient):
    create = await client.post("/<entities>/", json={...})
    entity_id = create.json()["id"]
    response = await client.delete(f"/<entities>/{entity_id}")
    assert response.status_code == 200
```

## Rules

- Always use the `client` fixture from `conftest.py`
- Create dependent entities within the test (don't rely on test order)
- Use unique values per test to avoid conflicts (unique emails, SKUs, etc.)
- Each test must be independent and repeatable
