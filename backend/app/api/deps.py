# app/api/deps.py
from typing import AsyncGenerator
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError
from sqlalchemy.ext.asyncio import AsyncSession
from azure.storage.blob import BlobServiceClient
from azure.cognitiveservices.speech import SpeechConfig

from app.db.session import AsyncSessionLocal
from app.core.config import settings
from app.core.security import verify_token
from app.models.user import User
from app.core.exceptions import CredentialsException

oauth2_scheme = OAuth2PasswordBearer(tokenUrl=f"{settings.API_V1_STR}/auth/login")

async def get_db() -> AsyncGenerator[AsyncSession, None]:
    """
    데이터베이스 세션 의존성
    """
    try:
        db = AsyncSessionLocal()
        yield db
    finally:
        await db.close()

async def get_current_user(
    db: AsyncSession = Depends(get_db),
    token: str = Depends(oauth2_scheme)
) -> User:
    """
    현재 인증된 사용자 가져오기
    """
    try:
        payload = verify_token(token)
        user_id: str = payload.get("sub")
        if user_id is None:
            raise CredentialsException()
    except JWTError:
        raise CredentialsException()
    
    user = await db.get(User, int(user_id))
    if user is None:
        raise CredentialsException()
    return user

async def get_current_active_user(
    current_user: User = Depends(get_current_user),
) -> User:
    """
    활성 사용자 확인
    """
    if not current_user.is_active:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user

def get_blob_client() -> BlobServiceClient:
    """
    Azure Blob Storage 클라이언트
    """
    return BlobServiceClient.from_connection_string(
        settings.AZURE_STORAGE_CONNECTION_STRING
    )

def get_speech_config() -> SpeechConfig:
    """
    Azure Speech 서비스 설정
    """
    return SpeechConfig(
        subscription=settings.AZURE_SPEECH_KEY,
        region=settings.AZURE_SPEECH_REGION
    )