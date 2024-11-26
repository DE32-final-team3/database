"""
from database import engine, SessionLocal
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from models import Base
from crud import create_track, update_track_details

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}

# 데이터베이스 테이블 생성
Base.metadata.create_all(bind=engine)

app = FastAPI()

# 의존성으로 데이터베이스 세션 제공
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/tracks/")
def add_track(track_data: dict, audio_features: dict = None, db: Session = Depends(get_db)):
    return create_track(db, track_data, audio_features)

@app.put("/tracks/{track_id}")
def update_track(track_id: str, track_details: dict, db: Session = Depends(get_db)):
    return update_track_details(db, track_id, track_details)
"""

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from schemas import TrackBase, TrackAudioFeatures
from crud import insert_track_info, update_audio_features
from models import Base, Track

app = FastAPI()
@app.on_event("startup")
async def startup():
    # This ensures the tables are created on app startup
    from database import engine
    # Make sure the tables are created
    Base.metadata.create_all(bind=engine)
# Track 기본 정보를 저장하는 엔드포인트
@app.post("/tracks/")
def create_tracks(tracks: list[TrackBase], db: Session = Depends(get_db)):
    insert_track_info(db, tracks)
    return {"message": "Tracks inserted or updated successfully"}

# Audio Features를 업데이트하는 엔드포인트
@app.put("/tracks/audio-features/")
def update_features(features: list[TrackAudioFeatures], db: Session = Depends(get_db)):
    update_audio_features(db, features)
    return {"message": "Audio features updated successfully"}

