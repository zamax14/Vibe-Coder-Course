from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.users.exceptions import UserAlreadyExistsException, UserNotFoundException
from app.users.models import User
from app.users.schemas import UserCreate, UserUpdate


async def get_all(session: AsyncSession) -> list[User]:
    result = await session.execute(select(User))
    return list(result.scalars().all())


async def get_by_id(session: AsyncSession, user_id: int) -> User:
    user = await session.get(User, user_id)
    if not user:
        raise UserNotFoundException()
    return user


async def create(session: AsyncSession, data: UserCreate) -> User:
    existing = await session.execute(select(User).where(User.email == data.email))
    if existing.scalar_one_or_none():
        raise UserAlreadyExistsException()

    user = User(**data.model_dump())
    session.add(user)
    await session.commit()
    await session.refresh(user)
    return user


async def update(session: AsyncSession, user_id: int, data: UserUpdate) -> User:
    user = await get_by_id(session, user_id)
    for field, value in data.model_dump(exclude_unset=True).items():
        setattr(user, field, value)
    await session.commit()
    await session.refresh(user)
    return user


async def delete(session: AsyncSession, user_id: int) -> dict:
    user = await get_by_id(session, user_id)
    await session.delete(user)
    await session.commit()
    return {"detail": "User deleted successfully"}
