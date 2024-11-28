from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.crud import add_follow

follow_router = APIRouter(prefix="/follow", tags=["Follow"])

@follow_router.post("/")
def follow_user(user_id: str, following_id: str, db: Session = Depends(get_db)):
    result = add_follow(db, user_id, following_id)
    return result