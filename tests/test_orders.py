import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_create_order(client: AsyncClient):
    user = await client.post("/users/", json={"name": "Buyer", "email": "buyer@example.com"})
    product = await client.post("/products/", json={"name": "Item", "sku": "ITM-001", "price": 50.00})

    response = await client.post("/orders/", json={
        "user_id": user.json()["id"],
        "product_id": product.json()["id"],
        "quantity": 2,
        "total_price": 100.00,
    })
    assert response.status_code == 201
    data = response.json()
    assert data["quantity"] == 2
    assert data["status"] == "pending"


@pytest.mark.asyncio
async def test_list_orders(client: AsyncClient):
    response = await client.get("/orders/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


@pytest.mark.asyncio
async def test_get_order_not_found(client: AsyncClient):
    response = await client.get("/orders/9999")
    assert response.status_code == 404


@pytest.mark.asyncio
async def test_update_order(client: AsyncClient):
    user = await client.post("/users/", json={"name": "Buyer2", "email": "buyer2@example.com"})
    product = await client.post("/products/", json={"name": "Item2", "sku": "ITM-002", "price": 25.00})
    order = await client.post("/orders/", json={
        "user_id": user.json()["id"],
        "product_id": product.json()["id"],
        "quantity": 1,
        "total_price": 25.00,
    })
    order_id = order.json()["id"]
    response = await client.put(f"/orders/{order_id}", json={"status": "confirmed"})
    assert response.status_code == 200
    assert response.json()["status"] == "confirmed"


@pytest.mark.asyncio
async def test_delete_order(client: AsyncClient):
    user = await client.post("/users/", json={"name": "Buyer3", "email": "buyer3@example.com"})
    product = await client.post("/products/", json={"name": "Item3", "sku": "ITM-003", "price": 10.00})
    order = await client.post("/orders/", json={
        "user_id": user.json()["id"],
        "product_id": product.json()["id"],
        "quantity": 1,
        "total_price": 10.00,
    })
    order_id = order.json()["id"]
    response = await client.delete(f"/orders/{order_id}")
    assert response.status_code == 200
