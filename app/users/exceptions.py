from fastapi import HTTPException, status

from app.users.constants import MESSAGES


class UserNotFoundException(HTTPException):
    def __init__(self) -> None:
        super().__init__(status_code=status.HTTP_404_NOT_FOUND, detail=MESSAGES["not_found"])


class UserAlreadyExistsException(HTTPException):
    def __init__(self) -> None:
        super().__init__(status_code=status.HTTP_409_CONFLICT, detail=MESSAGES["already_exists"])
