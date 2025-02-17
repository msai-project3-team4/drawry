# main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.api.v1 import api_router
from app.middleware.error_handler import error_handler_middleware

app = FastAPI(
    title=settings.PROJECT_NAME,
    description="Drawry API Documentation",  # API 문서 설명 추가
    version="1.0.0"  # 버전 정보 추가
)

# CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS_LIST,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 에러 핸들링 미들웨어
app.middleware("http")(error_handler_middleware)

# API 라우터 등록
app.include_router(api_router, prefix="/api/v1")