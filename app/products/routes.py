from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_session
from app.products import service
from app.products.schemas import ProductCreate, ProductResponse, ProductUpdate

router = APIRouter(prefix="/products", tags=["Products"])


@router.get("/", response_model=list[ProductResponse])
async def list_products(session: AsyncSession = Depends(get_session)) -> list[ProductResponse]:
    return await service.get_all(session)


@router.get("/{product_id}", response_model=ProductResponse)
async def get_product(product_id: int, session: AsyncSession = Depends(get_session)) -> ProductResponse:
    return await service.get_by_id(session, product_id)


@router.post("/", response_model=ProductResponse, status_code=status.HTTP_201_CREATED)
async def create_product(data: ProductCreate, session: AsyncSession = Depends(get_session)) -> ProductResponse:
    return await service.create(session, data)


@router.put("/{product_id}", response_model=ProductResponse)
async def update_product(
    product_id: int, data: ProductUpdate, session: AsyncSession = Depends(get_session)
) -> ProductResponse:
    return await service.update(session, product_id, data)


@router.delete("/{product_id}")
async def delete_product(product_id: int, session: AsyncSession = Depends(get_session)) -> dict:
    return await service.delete(session, product_id)
