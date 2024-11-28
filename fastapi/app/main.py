from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import engine
from app.models import Base
from app.router.track_router import track_router 
from app.router.playlist_router import playlist_router 
from app.router.follow_router import follow_router 
from app.router.taste_router import taste_router 

# 데이터베이스 테이블 생성
Base.metadata.create_all(bind=engine)

app = FastAPI()

# CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 모든 출처 허용 ("*" 대신 특정 도메인 리스트 가능)
    allow_credentials=True,
    allow_methods=["*"],  # 모든 HTTP 메서드 허용
    allow_headers=["*"],  # 모든 HTTP 헤더 허용
)

app.include_router(track_router)
app.include_router(playlist_router)
app.include_router(follow_router)
app.include_router(taste_router)
