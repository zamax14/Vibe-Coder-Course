from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel, ConfigDict


class OrderCreate(BaseModel):
    user_id: int
    product_id: int
    quantity: int = 1
    total_price: Decimal
    status: str = "pending"


class OrderUpdate(BaseModel):
    quantity: int | None = None
    total_price: Decimal | None = None
    status: str | None = None


class OrderResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    user_id: int
    product_id: int
    quantity: int
    total_price: Decimal
    status: str
    created_at: datetime
    updated_at: datetime
