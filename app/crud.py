# from sqlalchemy.orm import Session
# from models import Track

# def create_track(db: Session, track_data: dict, audio_features: dict = None):
#     new_track = Track(
#         id=track_data["id"],
#         name=track_data["name"],
#         artist=track_data["artist"],
#         image=track_data["image"]
#     )
#     db.add(new_track)
#     db.commit()
#     db.refresh(new_track)

#     if audio_features:
#         update_track_details(db, new_track.id, audio_features)

#     return {"success": f"Track '{new_track.name}' by {new_track.artist} 저장 및 업데이트 완료."}

# def update_track_details(db: Session, track_id: str, track_details: dict):
#     track = db.query(Track).filter(Track.id == track_id).first()
#     if not track:
#         return {"error": f"Track ID '{track_id}'를 찾을 수 없습니다."}

#     for key, value in track_details.items():
#         if hasattr(track, key) and value is not None:
#             setattr(track, key, value)

#     db.commit()
#     db.refresh(track)
#     return {"success": f"Track ID '{track_id}'의 오디오 피처가 성공적으로 업데이트되었습니다."}


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

