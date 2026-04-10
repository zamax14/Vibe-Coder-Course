from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_session
from app.users import service
from app.users.schemas import UserCreate, UserResponse, UserUpdate

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/", response_model=list[UserResponse])
async def list_users(session: AsyncSession = Depends(get_session)) -> list[UserResponse]:
    return await service.get_all(session)


@router.get("/{user_id}", response_model=UserResponse)
async def get_user(user_id: int, session: AsyncSession = Depends(get_session)) -> UserResponse:
    return await service.get_by_id(session, user_id)


@router.post("/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def create_user(data: UserCreate, session: AsyncSession = Depends(get_session)) -> UserResponse:
    return await service.create(session, data)


@router.put("/{user_id}", response_model=UserResponse)
async def update_user(
    user_id: int, data: UserUpdate, session: AsyncSession = Depends(get_session)
) -> UserResponse:
    return await service.update(session, user_id, data)


@router.delete("/{user_id}")
async def delete_user(user_id: int, session: AsyncSession = Depends(get_session)) -> dict:
    return await service.delete(session, user_id)
