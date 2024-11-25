from sqlalchemy.orm import Session
from models import Track
from schemas import TrackBase, TrackAudioFeatures

# Track 기본 정보를 저장하는 함수
def insert_track_info(db: Session, tracks: list[TrackBase]):
    for track in tracks:
        db_track = db.query(Track).filter(Track.id == track.id).first()
        if db_track:
            # 기존 데이터 업데이트
            db_track.name = track.name
            db_track.artist = track.artist
            db_track.image = track.image
        else:
            # 새 데이터 삽입
            db_track = Track(
                id=track.id,
                name=track.name,
                artist=track.artist,
                image=track.image
            )
            db.add(db_track)
    db.commit()

# Audio Features를 업데이트하는 함수
def update_audio_features(db: Session, features: list[TrackAudioFeatures]):
    for feature in features:
        db_track = db.query(Track).filter(Track.id == feature.id).first()
        if db_track:
            db_track.acousticness = feature.acousticness
            db_track.danceability = feature.danceability
            db_track.instrumentalness = feature.instrumentalness
            db_track.energy = feature.energy
            db_track.tempo = feature.tempo
            db_track.valence = feature.valence
            db_track.speechiness = feature.speechiness
    db.commit()

