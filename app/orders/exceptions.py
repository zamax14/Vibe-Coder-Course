from fastapi import HTTPException, status

from app.orders.constants import MESSAGES


class OrderNotFoundException(HTTPException):
    def __init__(self) -> None:
        super().__init__(status_code=status.HTTP_404_NOT_FOUND, detail=MESSAGES["not_found"])
