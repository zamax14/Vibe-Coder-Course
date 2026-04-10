---
description: "Use when writing or editing Python files. Covers type hints, async patterns, import ordering, and naming conventions for FastAPI projects."
applyTo: "**/*.py"
---
# Python API Conventions

## Imports Order

1. Standard library
2. Third-party packages (fastapi, sqlalchemy, pydantic)
3. Local imports (app.*)

Separate each group with a blank line.

## Async Patterns

- All database functions must be `async def`
- Use `await session.execute()` for queries
- Use `await session.commit()` after mutations
- Use `await session.refresh(instance)` after create/update

## Type Hints

- All function parameters must have type annotations
- All function return types must be annotated
- Use `list[Schema]` not `List[Schema]`
- Use `X | None` not `Optional[X]`

## Naming

- Files: `snake_case.py`
- Classes: `PascalCase`
- Functions/variables: `snake_case`
- Constants: `UPPER_SNAKE_CASE`
- Route paths: `kebab-case` or `snake_case` (prefer kebab)

## SQLAlchemy 2.0 Style

```python
# Correct
class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))

# Incorrect (old style)
class User(Base):
    id = Column(Integer, primary_key=True)
```

## Pydantic v2

```python
from pydantic import BaseModel, ConfigDict

class UserResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str
```
