from sqlalchemy import Column, String, Float, ForeignKey, PrimaryKeyConstraint
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Track(Base):
    __tablename__ = "track"

    id = Column(String(255), nullable=False, primary_key=True)
    name = Column(String(255), nullable=True)
    artist = Column(String(255), nullable=True)
    image = Column(String(255), nullable=True)
    acousticness = Column(Float, nullable=True)
    danceability = Column(Float, nullable=True)
    instrumentalness = Column(Float, nullable=True)
    energy = Column(Float, nullable=True)
    tempo = Column(Float, nullable=True)
    valence = Column(Float, nullable=True)
    speechiness = Column(Float, nullable=True)


class UserPlaylist(Base):
    __tablename__ = "user_playlist"

    user_id = Column(String(255), ForeignKey("user.ID"), nullable=False)
    track_id = Column(String(255), ForeignKey("track.id"), nullable=False)

    # 복합 기본 키 설정
    __table_args__ = (PrimaryKeyConstraint("user_id", "track_id"),)
