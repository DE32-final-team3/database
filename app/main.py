from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import engine, get_db
from schemas import TrackBase, TrackAudioFeatures, UserPlaylistBase
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


# 트랙 전체 데이터 가져오기
@app.get("/tracks/")
def get_tracks(db: Session = Depends(get_db)):
    tracks = get_all_tracks(db)
    return {"tracks": tracks}


# 특정 사용자의 플레이리스트에서 트랙 가져오기
@app.get("/user-playlist/{user_id}")
def get_user_tracks(user_id: str, db: Session = Depends(get_db)):
    tracks = get_tracks_by_user(db, user_id)
    return {"tracks": tracks}
