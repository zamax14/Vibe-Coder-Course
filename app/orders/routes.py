from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_session
from app.orders import service
from app.orders.schemas import OrderCreate, OrderResponse, OrderUpdate

router = APIRouter(prefix="/orders", tags=["Orders"])


@router.get("/", response_model=list[OrderResponse])
async def list_orders(session: AsyncSession = Depends(get_session)) -> list[OrderResponse]:
    return await service.get_all(session)


@router.get("/{order_id}", response_model=OrderResponse)
async def get_order(order_id: int, session: AsyncSession = Depends(get_session)) -> OrderResponse:
    return await service.get_by_id(session, order_id)


@router.post("/", response_model=OrderResponse, status_code=status.HTTP_201_CREATED)
async def create_order(data: OrderCreate, session: AsyncSession = Depends(get_session)) -> OrderResponse:
    return await service.create(session, data)


@router.put("/{order_id}", response_model=OrderResponse)
async def update_order(
    order_id: int, data: OrderUpdate, session: AsyncSession = Depends(get_session)
) -> OrderResponse:
    return await service.update(session, order_id, data)


@router.delete("/{order_id}")
async def delete_order(order_id: int, session: AsyncSession = Depends(get_session)) -> dict:
    return await service.delete(session, order_id)
