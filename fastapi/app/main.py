from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db, engine
from app.schemas import TrackBase, TrackAudioFeatures, UserPlaylistBase
from app.crud import insert_track_info, update_audio_features, add_to_playlist, remove_from_playlist
from app.models import Base

# 데이터베이스 테이블 생성
Base.metadata.create_all(bind=engine)

app = FastAPI()

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


# 사용자 플레이리스트에 트랙 추가
@app.post("/user-playlist/")
def add_track(playlist: UserPlaylistBase, db: Session = Depends(get_db)):
    add_to_playlist(db, playlist)
    return {"message": "Track added to playlist successfully"}

# 사용자 플레이리스트에서 트랙 제거
@app.delete("/user-playlist/")
def remove_track(playlist: UserPlaylistBase, db: Session = Depends(get_db)):
    remove_from_playlist(db, playlist)
    return {"message": "Track removed from playlist successfully"}
