from pydantic import BaseModel
from typing import Optional

class TrackBase(BaseModel):
    id: str
    name: Optional[str]
    artist: Optional[str]
    image: Optional[str]

class TrackAudioFeatures(BaseModel):
    id: str
    acousticness: Optional[float]
    danceability: Optional[float]
    instrumentalness: Optional[float]
    energy: Optional[float]
    tempo: Optional[float]
    valence: Optional[float]
    speechiness: Optional[float]

