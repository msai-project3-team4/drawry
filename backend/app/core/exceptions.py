from fastapi import HTTPException, status

class DrawryException(HTTPException):
    def __init__(
        self,
        status_code: int,
        message: str,
    ):
        super().__init__(status_code=status_code, detail=message)

class CredentialsException(DrawryException):
    def __init__(self):
        super().__init__(
            status_code=status.HTTP_401_UNAUTHORIZED,
            message="Could not validate credentials"
        )