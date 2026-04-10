import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_create_product(client: AsyncClient):
    response = await client.post("/products/", json={
        "name": "Laptop", "sku": "LAP-001", "price": 999.99, "stock": 10
    })
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "Laptop"
    assert data["sku"] == "LAP-001"


@pytest.mark.asyncio
async def test_list_products(client: AsyncClient):
    await client.post("/products/", json={"name": "Mouse", "sku": "MOU-001", "price": 29.99})
    response = await client.get("/products/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


@pytest.mark.asyncio
async def test_get_product(client: AsyncClient):
    create = await client.post("/products/", json={"name": "Keyboard", "sku": "KEY-001", "price": 79.99})
    product_id = create.json()["id"]
    response = await client.get(f"/products/{product_id}")
    assert response.status_code == 200
    assert response.json()["name"] == "Keyboard"


@pytest.mark.asyncio
async def test_get_product_not_found(client: AsyncClient):
    response = await client.get("/products/9999")
    assert response.status_code == 404


@pytest.mark.asyncio
async def test_update_product(client: AsyncClient):
    create = await client.post("/products/", json={"name": "Monitor", "sku": "MON-001", "price": 399.99})
    product_id = create.json()["id"]
    response = await client.put(f"/products/{product_id}", json={"price": 349.99})
    assert response.status_code == 200
    assert float(response.json()["price"]) == 349.99


@pytest.mark.asyncio
async def test_delete_product(client: AsyncClient):
    create = await client.post("/products/", json={"name": "Headset", "sku": "HEA-001", "price": 59.99})
    product_id = create.json()["id"]
    response = await client.delete(f"/products/{product_id}")
    assert response.status_code == 200
