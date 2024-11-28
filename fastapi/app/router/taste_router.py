from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas import UserTasteBase
from app.crud import update_user_taste

taste_router = APIRouter(prefix="/user-taste", tags=["UserTaste"])

@taste_router.post("/add")
def update_tastes(tastes: list[UserTasteBase], db: Session = Depends(get_db)):
    update_user_taste(db, tastes=[taste.dict() for taste in tastes])
    return {"message": "User tastes updated successfully"}
