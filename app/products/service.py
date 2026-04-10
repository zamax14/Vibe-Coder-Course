from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.products.exceptions import ProductAlreadyExistsException, ProductNotFoundException
from app.products.models import Product
from app.products.schemas import ProductCreate, ProductUpdate


async def get_all(session: AsyncSession) -> list[Product]:
    result = await session.execute(select(Product))
    return list(result.scalars().all())


async def get_by_id(session: AsyncSession, product_id: int) -> Product:
    product = await session.get(Product, product_id)
    if not product:
        raise ProductNotFoundException()
    return product


async def create(session: AsyncSession, data: ProductCreate) -> Product:
    existing = await session.execute(select(Product).where(Product.sku == data.sku))
    if existing.scalar_one_or_none():
        raise ProductAlreadyExistsException()

    product = Product(**data.model_dump())
    session.add(product)
    await session.commit()
    await session.refresh(product)
    return product


async def update(session: AsyncSession, product_id: int, data: ProductUpdate) -> Product:
    product = await get_by_id(session, product_id)
    for field, value in data.model_dump(exclude_unset=True).items():
        setattr(product, field, value)
    await session.commit()
    await session.refresh(product)
    return product


async def delete(session: AsyncSession, product_id: int) -> dict:
    product = await get_by_id(session, product_id)
    await session.delete(product)
    await session.commit()
    return {"detail": "Product deleted successfully"}
