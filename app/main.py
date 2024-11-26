from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import engine, get_db
from schemas import TrackBase, TrackAudioFeatures
from crud import insert_track_info, update_audio_features
from models import Base, Track

app = FastAPI()
@app.on_event("startup")
async def startup():
    # This ensures the tables are created on app startup
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

