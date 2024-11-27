from sqlalchemy import Column, String, Float, ForeignKey, PrimaryKeyConstraint, DateTime
from sqlalchemy.orm import declarative_base
import uuid

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

    user_id = Column(String(255), ForeignKey("user.id"), nullable=False)
    track_id = Column(String(255), ForeignKey("track.id"), nullable=False)

    __table_args__ = (PrimaryKeyConstraint("user_id", "track_id"),)


class User(Base):
    __tablename__ = "user"
    id = Column(
        String(255), primary_key=True, default=lambda: str(uuid.uuid4()), nullable=False
    )
    email = Column(String(255), unique=True, nullable=False)
    nickname = Column(String(255), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    profile = Column(String(255), nullable=False)
    create_at = Column(DateTime(timezone=True))


class Following(Base):
    __tablename__ = "following"

    following = Column(String(255), ForeignKey("user.id"), nullable=False)
    follower = Column(String(255), ForeignKey("user.id"), nullable=False)

    __table_args__ = (PrimaryKeyConstraint("following", "follower"),)


class UserTaste(Base):
    __tablename__ = "user_taste"

    user_id = Column(String(255), ForeignKey("user.id"), primary_key=True)
    acousticness = Column(Float, nullable=True)
    danceability = Column(Float, nullable=True)
    instrumentalness = Column(Float, nullable=True)
    energy = Column(Float, nullable=True)
    tempo = Column(Float, nullable=True)
    valence = Column(Float, nullable=True)
    speechiness = Column(Float, nullable=True)