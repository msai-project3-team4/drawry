from fastapi import HTTPException, status

class DrawryException(HTTPException):
    """
    기본 예외 클래스
    """
    def __init__(
        self,
        status_code: int,
        detail: str,
        headers: dict = None
    ):
        super().__init__(status_code=status_code, detail=detail, headers=headers)

class CredentialsException(DrawryException):
    """
    인증 실패 예외
    """
    def __init__(self):
        super().__init__(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"}
        )

class NotFoundError(DrawryException):
    """
    리소스를 찾을 수 없을 때의 예외
    """
    def __init__(self, resource: str):
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"{resource} not found"
        )

class ValidationError(DrawryException):
    """
    입력값 검증 실패 예외
    """
    def __init__(self, detail: str):
        super().__init__(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=detail
        )

class AzureServiceError(DrawryException):
    """
    Azure 서비스 관련 예외
    """
    def __init__(self, service: str, detail: str):
        super().__init__(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail=f"Azure {service} service error: {detail}"
        )