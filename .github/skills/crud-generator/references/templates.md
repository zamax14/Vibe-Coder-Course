# Module Templates

Reference templates for each file in a CRUD module. Replace `<Entity>` with entity name (PascalCase), `<entity>` with snake_case, `<entities>` with plural.

## constants.py

```python
ENTITY_NAME = "<Entity>"

MESSAGES = {
    "not_found": "<Entity> not found",
    "created": "<Entity> created successfully",
    "updated": "<Entity> updated successfully",
    "deleted": "<Entity> deleted successfully",
    "already_exists": "<Entity> already exists",
}
```

## exceptions.py

```python
from fastapi import HTTPException, status
from app.<entity>.constants import MESSAGES


class <Entity>NotFoundException(HTTPException):
    def __init__(self) -> None:
        super().__init__(status_code=status.HTTP_404_NOT_FOUND, detail=MESSAGES["not_found"])


class <Entity>AlreadyExistsException(HTTPException):
    def __init__(self) -> None:
        super().__init__(status_code=status.HTTP_409_CONFLICT, detail=MESSAGES["already_exists"])
```

## models.py

```python
from datetime import datetime
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base


class <Entity>(Base):
    __tablename__ = "<entities>"

    id: Mapped[int] = mapped_column(primary_key=True)
    # ... entity-specific fields ...
    created_at: Mapped[datetime] = mapped_column(default_factory=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(default_factory=datetime.utcnow, onupdate=datetime.utcnow)
```

**Field type mapping:**
- `str` → `Mapped[str] = mapped_column(String(N))`
- `str | None` → `Mapped[str | None] = mapped_column(String(N), nullable=True)`
- `int` → `Mapped[int]`
- `Decimal` → `Mapped[Decimal] = mapped_column(Numeric(10, 2))`
- `bool` → `Mapped[bool] = mapped_column(default=True)`
- Foreign key → `Mapped[int] = mapped_column(ForeignKey("table.id"))`

## schemas.py

```python
from datetime import datetime
from pydantic import BaseModel, ConfigDict


class <Entity>Create(BaseModel):
    # All required fields for creation
    pass


class <Entity>Update(BaseModel):
    # All fields optional
    pass


class <Entity>Response(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    # ... all fields ...
    created_at: datetime
    updated_at: datetime
```

## service.py

```python
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.<entity>.exceptions import <Entity>NotFoundException
from app.<entity>.models import <Entity>
from app.<entity>.schemas import <Entity>Create, <Entity>Update


async def get_all(session: AsyncSession) -> list[<Entity>]:
    result = await session.execute(select(<Entity>))
    return list(result.scalars().all())


async def get_by_id(session: AsyncSession, <entity>_id: int) -> <Entity>:
    <entity> = await session.get(<Entity>, <entity>_id)
    if not <entity>:
        raise <Entity>NotFoundException()
    return <entity>


async def create(session: AsyncSession, data: <Entity>Create) -> <Entity>:
    <entity> = <Entity>(**data.model_dump())
    session.add(<entity>)
    await session.commit()
    await session.refresh(<entity>)
    return <entity>


async def update(session: AsyncSession, <entity>_id: int, data: <Entity>Update) -> <Entity>:
    <entity> = await get_by_id(session, <entity>_id)
    for field, value in data.model_dump(exclude_unset=True).items():
        setattr(<entity>, field, value)
    await session.commit()
    await session.refresh(<entity>)
    return <entity>


async def delete(session: AsyncSession, <entity>_id: int) -> dict:
    <entity> = await get_by_id(session, <entity>_id)
    await session.delete(<entity>)
    await session.commit()
    return {"detail": "<Entity> deleted successfully"}
```

## routes.py

```python
from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_session
from app.<entity> import service
from app.<entity>.schemas import <Entity>Create, <Entity>Response, <Entity>Update

router = APIRouter(prefix="/<entities>", tags=["<Entities>"])


@router.get("/", response_model=list[<Entity>Response])
async def list_<entities>(session: AsyncSession = Depends(get_session)) -> list[<Entity>Response]:
    return await service.get_all(session)


@router.get("/{<entity>_id}", response_model=<Entity>Response)
async def get_<entity>(<entity>_id: int, session: AsyncSession = Depends(get_session)) -> <Entity>Response:
    return await service.get_by_id(session, <entity>_id)


@router.post("/", response_model=<Entity>Response, status_code=status.HTTP_201_CREATED)
async def create_<entity>(data: <Entity>Create, session: AsyncSession = Depends(get_session)) -> <Entity>Response:
    return await service.create(session, data)


@router.put("/{<entity>_id}", response_model=<Entity>Response)
async def update_<entity>(<entity>_id: int, data: <Entity>Update, session: AsyncSession = Depends(get_session)) -> <Entity>Response:
    return await service.update(session, <entity>_id, data)


@router.delete("/{<entity>_id}")
async def delete_<entity>(<entity>_id: int, session: AsyncSession = Depends(get_session)) -> dict:
    return await service.delete(session, <entity>_id)
```
