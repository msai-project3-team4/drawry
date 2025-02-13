import os
import pathlib
from typing import List

def create_directory_structure() -> None:
    """현재 디렉토리에 프로젝트 구조를 생성합니다."""
    
    # 현재 작업 디렉토리 확인
    base_dir = os.getcwd()
    
    # 생성할 디렉토리 경로 목록
    directories = [
        "alembic/versions",
        "app/api/v1/endpoints",
        "app/core",
        "app/db",
        "app/models",
        "app/schemas",
        "app/services/azure",
        "app/tasks",
        "app/utils",
        "tests/api",
        "tests/services",
    ]
    
    # 생성할 파일 목록
    files = [
        # API 엔드포인트
        "app/api/v1/endpoints/auth.py",
        "app/api/v1/endpoints/profile.py",
        "app/api/v1/endpoints/books.py",
        "app/api/v1/endpoints/stories.py",
        "app/api/v1/endpoints/sketches.py",
        "app/api/v1/endpoints/tracking.py",
        "app/api/v1/endpoints/games.py",
        "app/api/v1/api.py",
        "app/api/deps.py",
        
        # 코어 설정
        "app/core/config.py",
        "app/core/security.py",
        "app/core/exceptions.py",
        "app/core/responses.py",
        
        # 데이터베이스
        "app/db/base.py",
        "app/db/session.py",
        
        # 모델
        "app/models/user.py",
        "app/models/profile.py",
        "app/models/book.py",
        "app/models/story.py",
        "app/models/sketch.py",
        "app/models/tracking.py",
        "app/models/game.py",
        
        # 스키마
        "app/schemas/user.py",
        "app/schemas/profile.py",
        "app/schemas/book.py",
        "app/schemas/story.py",
        "app/schemas/sketch.py",
        "app/schemas/tracking.py",
        "app/schemas/game.py",
        
        # 서비스
        "app/services/azure/speech.py",
        "app/services/azure/storage.py",
        "app/services/azure/openai.py",
        "app/services/azure/controlnet.py",
        "app/services/auth.py",
        "app/services/profile.py",
        "app/services/story.py",
        "app/services/eye_tracker.py",
        "app/services/game.py",
        
        # 태스크
        "app/tasks/generation.py",
        
        # 유틸리티
        "app/utils/file_handlers.py",
        "app/utils/validators.py",
        
        # 테스트
        "tests/conftest.py",
        
        # 루트 파일들
        ".env",
        ".gitignore",
        "alembic.ini",
        "main.py",
        "pyproject.toml",
        "requirements.txt"
    ]
    
    try:
        # 디렉토리 생성
        for directory in directories:
            dir_path = os.path.join(base_dir, directory)
            os.makedirs(dir_path, exist_ok=True)
            # __init__.py 파일 생성
            init_file = os.path.join(dir_path, "__init__.py")
            pathlib.Path(init_file).touch()
        
        # 파일 생성
        for file in files:
            file_path = os.path.join(base_dir, file)
            directory = os.path.dirname(file_path)
            if not os.path.exists(directory):
                os.makedirs(directory)
            pathlib.Path(file_path).touch()
            
        print(f"디렉토리 구조가 {base_dir}에 생성되었습니다.")
            
    except Exception as e:
        print(f"디렉토리 구조 생성 중 오류 발생: {str(e)}")

def create_gitignore() -> None:
    """기본 .gitignore 파일을 생성합니다."""
    content = """# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
env/
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# Virtual Environment
venv/
ENV/

# IDE
.idea/
.vscode/
*.swp
*.swo

# Environment variables
.env

# Database
*.db
*.sqlite3

# Logs
*.log

# Unit test / coverage reports
htmlcov/
.tox/
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*.cover
.hypothesis/

# Azure
*.pubxml
*.publishsettings
"""
    
    try:
        with open(".gitignore", "w", encoding="utf-8") as f:
            f.write(content)
        print(".gitignore 파일이 생성되었습니다.")
    except Exception as e:
        print(f".gitignore 파일 생성 중 오류 발생: {str(e)}")

def create_requirements() -> None:
    """기본 requirements.txt 파일을 생성합니다."""
    content = """# FastAPI framework
fastapi>=0.68.0
uvicorn>=0.15.0
pydantic>=1.8.0
email-validator>=1.1.3

# Database
sqlalchemy>=1.4.23
alembic>=1.7.1
aiosqlite>=0.17.0

# Authentication
python-jose[cryptography]>=3.3.0
passlib[bcrypt]>=1.7.4
python-multipart>=0.0.5

# Azure Services
azure-cognitiveservices-speech>=1.19.0
azure-storage-blob>=12.9.0
openai>=0.27.0

# Utilities
python-dotenv>=0.19.0
aiofiles>=0.7.0
Pillow>=8.3.2

# Testing
pytest>=6.2.5
pytest-asyncio>=0.15.1
httpx>=0.19.0
"""
    
    try:
        with open("requirements.txt", "w", encoding="utf-8") as f:
            f.write(content)
        print("requirements.txt 파일이 생성되었습니다.")
    except Exception as e:
        print(f"requirements.txt 파일 생성 중 오류 발생: {str(e)}")

def main():
    """메인 실행 함수"""
    print("프로젝트 구조 생성을 시작합니다...")
    try:
        # 디렉토리 구조 생성
        create_directory_structure()
        
        # .gitignore 파일 생성
        create_gitignore()
        
        # requirements.txt 파일 생성
        create_requirements()
        
        print("프로젝트 구조가 성공적으로 생성되었습니다!")
        
    except Exception as e:
        print(f"프로젝트 생성 중 에러 발생: {str(e)}")

if __name__ == "__main__":
    main()


'''
drawry/
├── alembic/                    # 데이터베이스 마이그레이션 관리
│   └── versions/               # 마이그레이션 버전 파일들 저장
├── app/
│   ├── api/                    # API 관련 모듈
│   │   ├── v1/                # API 버전 1
│   │   │   ├── endpoints/     # 엔드포인트 정의
│   │   │   │   ├── auth.py    # 인증 관련 API (로그인, 회원가입, 토큰 재발급)
│   │   │   │   ├── profile.py # 프로필 관리 API (별명, 생일 설정)
│   │   │   │   ├── books.py   # 동화책 CRUD API (목록, 생성, 수정, 삭제)
│   │   │   │   ├── stories.py # 스토리 생성 API (RAG 기반 스토리 생성)
│   │   │   │   ├── sketches.py # 스케치 관련 API (업로드, 이미지 생성)
│   │   │   │   ├── tracking.py # 학습 모니터링 API (아이트래커 데이터 저장)
│   │   │   │   └── games.py    # 게임 관련 API (결과 저장, 통계)
│   │   │   └── api.py         # 모든 API 라우터 통합
│   │   └── deps.py            # 의존성 주입 (인증, DB 세션, 권한 체크)
│   ├── core/                   # 핵심 설정 및 유틸리티
│   │   ├── config.py          # 환경변수 및 앱 설정 관리
│   │   ├── security.py        # 보안 관련 (JWT 생성/검증, 비밀번호 해싱)
│   │   ├── exceptions.py      # 커스텀 예외 클래스 정의
│   │   └── responses.py       # 표준 응답 형식 정의
│   ├── db/                     # 데이터베이스 관련
│   │   ├── base.py            # SQLAlchemy 모델 기본 클래스 및 설정
│   │   └── session.py         # 데이터베이스 세션 관리
│   ├── models/                 # SQLAlchemy 모델 정의
│   │   ├── user.py            # 사용자 모델 (이메일, 비밀번호)
│   │   ├── profile.py         # 프로필 모델 (별명, 생일)
│   │   ├── book.py            # 동화책 모델 (제목, 생성일, 소유자)
│   │   ├── story.py           # 스토리 모델 (페이지별 내용)
│   │   ├── sketch.py          # 스케치 모델 (원본, 생성된 이미지)
│   │   ├── tracking.py        # 학습 추적 모델 (아이트래커 데이터)
│   │   └── game.py            # 게임 결과 모델 (점수, 완료 시간)
│   ├── schemas/               # Pydantic 모델 (요청/응답 스키마)
│   │   ├── user.py           # 사용자 스키마 (회원가입, 로그인)
│   │   ├── profile.py        # 프로필 스키마 (정보 수정)
│   │   ├── book.py           # 동화책 스키마 (생성, 수정)
│   │   ├── story.py          # 스토리 스키마 (생성 요청/응답)
│   │   ├── sketch.py         # 스케치 스키마 (업로드, 생성)
│   │   ├── tracking.py       # 트래킹 데이터 스키마
│   │   └── game.py           # 게임 데이터 스키마
│   ├── services/              # 비즈니스 로직
│   │   ├── azure/            # Azure 서비스 통합
│   │   │   ├── speech.py     # Speech Services 연동 (TTS/STT)
│   │   │   ├── storage.py    # Blob Storage 연동 (이미지 저장)
│   │   │   ├── openai.py     # OpenAI 연동 (RAG)
│   │   │   └── controlnet.py # ControlNet 연동 (이미지 생성)
│   │   ├── auth.py           # 인증 관련 비즈니스 로직
│   │   ├── profile.py        # 프로필 관리 로직
│   │   ├── story.py          # 스토리 생성 로직
│   │   ├── eye_tracker.py    # 아이트래커 처리 로직
│   │   └── game.py           # 게임 관련 비즈니스 로직
│   ├── tasks/                 # 백그라운드 작업
│   │   └── generation.py      # 이미지 생성 작업 처리
│   └── utils/                 # 유틸리티 함수
│       ├── file_handlers.py   # 파일 업로드/다운로드 처리
│       └── validators.py      # 데이터 유효성 검사
├── tests/                     # 테스트 코드
│   ├── api/                   # API 테스트
│   ├── services/             # 서비스 테스트
│   └── conftest.py           # pytest 설정
├── .env                      # 환경변수 파일
├── .gitignore               # git 제외 파일 설정
├── alembic.ini              # Alembic 설정
├── main.py                  # FastAPI 앱 초기화 및 설정
├── pyproject.toml          # 프로젝트 메타데이터
└── requirements.txt        # 프로젝트 의존성 목록
'''