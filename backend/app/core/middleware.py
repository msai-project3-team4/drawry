import logging
import time
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException
from app.core.exceptions import DrawryException, HTTPException

# 로깅 설정
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def setup_middleware(app: FastAPI) -> None:
    """
    미들웨어 설정 함수
    """
    
    # FastAPI의 기본 HTTPException 핸들러
    @app.exception_handler(StarletteHTTPException)
    async def http_exception_handler(request, exc):
        return JSONResponse(
            status_code=exc.status_code,
            content={
                "success": False,
                "error": str(exc.detail)
            }
        )
    
    # 유효성 검사 예외 핸들러
    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(request, exc):
        return JSONResponse(
            status_code=422,
            content={
                "success": False,
                "error": "Validation error",
                "detail": str(exc)
            }
        )

    @app.middleware("http")
    async def error_handling_middleware(request: Request, call_next):
        try:
            response = await call_next(request)
            return response
        except (DrawryException, HTTPException) as exc:
            return JSONResponse(
                status_code=exc.status_code,
                content={
                    "success": False,
                    "error": exc.detail
                }
            )
        except Exception as exc:
            logger.error(f"Unexpected error: {str(exc)}")
            return JSONResponse(
                status_code=500,
                content={
                    "success": False,
                    "error": "Internal server error",
                    "detail": str(exc)
                }
            )

    @app.middleware("http")
    async def logging_middleware(request: Request, call_next):
        """
        로깅 미들웨어
        """
        start_time = time.time()
        
        # 요청 로깅
        logger.info(f"Request: {request.method} {request.url.path}")
        
        response = await call_next(request)
        
        # 처리 시간 계산 및 로깅
        process_time = time.time() - start_time
        logger.info(
            f"Response: {response.status_code} "
            f"Path: {request.url.path} "
            f"Method: {request.method} "
            f"Processing Time: {process_time:.2f}s"
        )
        
        return response

    # CORS 미들웨어 설정
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # 프로덕션에서는 실제 도메인으로 변경
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )