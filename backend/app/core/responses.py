from typing import Generic, TypeVar, Optional, List, Any
from pydantic import BaseModel

T = TypeVar('T')

class BaseResponse(BaseModel):
    """
    기본 응답 모델
    """
    success: bool
    message: str
    data: Optional[Any] = None

class ErrorResponse(BaseModel):
    """
    에러 응답 모델
    """
    success: bool = False
    error: str
    detail: Optional[str] = None

class PaginatedResponse(BaseModel, Generic[T]):
    """
    페이지네이션 응답 모델
    """
    success: bool = True
    total: int
    page: int
    size: int
    items: List[T]