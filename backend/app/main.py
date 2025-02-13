from fastapi import FastAPI
from app.core.middleware import setup_middleware
from app.core.config import settings

app = FastAPI(
    title=settings.PROJECT_NAME,
    description="API for Drawry - Interactive storytelling for dyslexic children",
    version=settings.VERSION,
)

# 미들웨어 설정
setup_middleware(app)

@app.get("/")
async def root():
    return {
        "success": True,
        "message": "Welcome to Drawry API",
        "version": settings.VERSION
    }

from fastapi import Depends, HTTPException
from app.api.deps import get_db, get_current_user
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.exceptions import DrawryException, NotFoundError
from typing import Dict
from sqlalchemy import text

# 1. 데이터베이스 연결 테스트
@app.get("/test/db", tags=["test"])
async def test_db(db: AsyncSession = Depends(get_db)) -> Dict:
    try:
        query = text("SELECT 1")
        await db.execute(query)
        return {
            "success": True,
            "message": "Database connection successful"
        }
    except Exception as e:
        return {
            "success": False,
            "message": f"Database connection failed: {str(e)}"
        }

# 2. 에러 핸들링 테스트
@app.get("/test/error/{error_type}", tags=["test"])
async def test_error(error_type: str) -> Dict:
    if error_type == "http":
        raise HTTPException(status_code=400, detail="Test HTTP exception")
    elif error_type == "custom":
        raise NotFoundError("Test resource")
    elif error_type == "unhandled":
        raise ValueError("Test unhandled error")
    return {"success": True, "message": "No error"}

# 3. 미들웨어 로깅 테스트
@app.get("/test/logging", tags=["test"])
async def test_logging() -> Dict:
    return {
        "success": True,
        "message": "Check your console/logs for the request details"
    }

