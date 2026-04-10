from fastapi import HTTPException, status

from app.products.constants import MESSAGES


class ProductNotFoundException(HTTPException):
    def __init__(self) -> None:
        super().__init__(status_code=status.HTTP_404_NOT_FOUND, detail=MESSAGES["not_found"])


class ProductAlreadyExistsException(HTTPException):
    def __init__(self) -> None:
        super().__init__(status_code=status.HTTP_409_CONFLICT, detail=MESSAGES["already_exists"])
