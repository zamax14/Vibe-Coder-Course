from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.orders.exceptions import OrderNotFoundException
from app.orders.models import Order
from app.orders.schemas import OrderCreate, OrderUpdate


async def get_all(session: AsyncSession) -> list[Order]:
    result = await session.execute(select(Order))
    return list(result.scalars().all())


async def get_by_id(session: AsyncSession, order_id: int) -> Order:
    order = await session.get(Order, order_id)
    if not order:
        raise OrderNotFoundException()
    return order


async def create(session: AsyncSession, data: OrderCreate) -> Order:
    order = Order(**data.model_dump())
    session.add(order)
    await session.commit()
    await session.refresh(order)
    return order


async def update(session: AsyncSession, order_id: int, data: OrderUpdate) -> Order:
    order = await get_by_id(session, order_id)
    for field, value in data.model_dump(exclude_unset=True).items():
        setattr(order, field, value)
    await session.commit()
    await session.refresh(order)
    return order


async def delete(session: AsyncSession, order_id: int) -> dict:
    order = await get_by_id(session, order_id)
    await session.delete(order)
    await session.commit()
    return {"detail": "Order deleted successfully"}
