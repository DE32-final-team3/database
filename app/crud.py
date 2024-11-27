from sqlalchemy.orm import Session
from models import Track, UserPlaylist, Following, UserTaste
from schemas import TrackBase, TrackAudioFeatures, UserPlaylistBase

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

# 플레이리스트에 트랙 추가
def add_to_playlist(db: Session, playlist: UserPlaylistBase):
    existing_entry = (
        db.query(UserPlaylist)
        .filter(
            UserPlaylist.user_id == playlist.user_id,
            UserPlaylist.track_id == playlist.track_id,
        )
        .first()
    )
    if not existing_entry:
        db_entry = UserPlaylist(
            user_id=playlist.user_id,
            track_id=playlist.track_id,
        )
        db.add(db_entry)
        db.commit()

# 플레이리스트에서 트랙 제거
def remove_from_playlist(db: Session, playlist: UserPlaylistBase):
    db_entry = (
        db.query(UserPlaylist)
        .filter(
            UserPlaylist.user_id == playlist.user_id,
            UserPlaylist.track_id == playlist.track_id,
        )
        .first()
    )
    if db_entry:
        db.delete(db_entry)
        db.commit()


# 트랙 전체 데이터 가져오기
def get_all_tracks(db: Session):
    tracks = db.query(Track).all()
    return [
        {
            "id": track.id,
            "name": track.name,
            "artist": track.artist,
            "image": track.image,
            "acousticness": track.acousticness,
            "danceability": track.danceability,
            "instrumentalness": track.instrumentalness,
            "energy": track.energy,
            "tempo": track.tempo,
            "valence": track.valence,
            "speechiness": track.speechiness,
        }
        for track in tracks
    ]


# 특정 사용자의 플레이리스트에서 트랙 가져오기
def get_tracks_by_user(db: Session, user_id: str):
    tracks = (
        db.query(Track)
        .join(UserPlaylist, Track.id == UserPlaylist.track_id)
        .filter(UserPlaylist.user_id == user_id)
        .all()
    )
    return [
        {
            "id": track.id,
            "name": track.name,
            "artist": track.artist,
            "image": track.image,
            "acousticness": track.acousticness,
            "danceability": track.danceability,
            "instrumentalness": track.instrumentalness,
            "energy": track.energy,
            "tempo": track.tempo,
            "valence": track.valence,
            "speechiness": track.speechiness,
        }
        for track in tracks
    ]

# 팔로잉 팔로우
def add_follow(db: Session, user_id: str, follower_id: str):
    # Check if the follow relationship already exists
    existing = (
        db.query(Following)
        .filter(
            Following.following == user_id,
            Following.follower == follower_id,
        )
        .first()
    )
    if not existing:
        # Create new follow relationship
        follow = Following(
            following=user_id,
            follower=follower_id,
        )
        db.add(follow)
        db.commit()
        return {"message": f"User {user_id} is now following {follower_id}"}
    else:
        return {"message": f"User {user_id} is already following {follower_id}"}
    


# 특정 사용자의 취향 분석 결과 저장 업데이트 
def update_user_taste(db: Session, tastes: list[dict]):
    for taste in tastes:
        # Query the UserTaste table
        existing_taste = db.query(UserTaste).filter(UserTaste.user_id == taste["user_id"]).first()
        if existing_taste:
            # Update existing user taste
            existing_taste.acousticness = taste.get("acousticness", existing_taste.acousticness)
            existing_taste.danceability = taste.get("danceability", existing_taste.danceability)
            existing_taste.instrumentalness = taste.get("instrumentalness", existing_taste.instrumentalness)
            existing_taste.energy = taste.get("energy", existing_taste.energy)
            existing_taste.tempo = taste.get("tempo", existing_taste.tempo)
            existing_taste.valence = taste.get("valence", existing_taste.valence)
            existing_taste.speechiness = taste.get("speechiness", existing_taste.speechiness)
        else:
            # Insert a new user taste
            new_taste = UserTaste(
                user_id=taste["user_id"],
                acousticness=taste.get("acousticness"),
                danceability=taste.get("danceability"),
                instrumentalness=taste.get("instrumentalness"),
                energy=taste.get("energy"),
                tempo=taste.get("tempo"),
                valence=taste.get("valence"),
                speechiness=taste.get("speechiness"),
            )
            db.add(new_taste)
    db.commit()
