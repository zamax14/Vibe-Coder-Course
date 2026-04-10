import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_create_user(client: AsyncClient):
    response = await client.post("/users/", json={"name": "John Doe", "email": "john@example.com"})
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "John Doe"
    assert data["email"] == "john@example.com"
    assert data["is_active"] is True


@pytest.mark.asyncio
async def test_list_users(client: AsyncClient):
    await client.post("/users/", json={"name": "Jane", "email": "jane@example.com"})
    response = await client.get("/users/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


@pytest.mark.asyncio
async def test_get_user(client: AsyncClient):
    create = await client.post("/users/", json={"name": "Bob", "email": "bob@example.com"})
    user_id = create.json()["id"]
    response = await client.get(f"/users/{user_id}")
    assert response.status_code == 200
    assert response.json()["name"] == "Bob"


@pytest.mark.asyncio
async def test_get_user_not_found(client: AsyncClient):
    response = await client.get("/users/9999")
    assert response.status_code == 404


@pytest.mark.asyncio
async def test_update_user(client: AsyncClient):
    create = await client.post("/users/", json={"name": "Alice", "email": "alice@example.com"})
    user_id = create.json()["id"]
    response = await client.put(f"/users/{user_id}", json={"name": "Alice Updated"})
    assert response.status_code == 200
    assert response.json()["name"] == "Alice Updated"


@pytest.mark.asyncio
async def test_delete_user(client: AsyncClient):
    create = await client.post("/users/", json={"name": "ToDelete", "email": "delete@example.com"})
    user_id = create.json()["id"]
    response = await client.delete(f"/users/{user_id}")
    assert response.status_code == 200
