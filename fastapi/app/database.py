from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
import os

# Load database configuration from environment variables
DB_USER = os.getenv("DB_USER", "tune")
DB_PASSWORD = os.getenv("DB_PASSWORD", "talk")
DB_HOST = os.getenv("DB_HOST", "mariadb")
DB_PORT = os.getenv("DB_PORT", "3306")
DB_NAME = os.getenv("DB_NAME", "tunetalk")

# SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:team3@mariadb:3306/spotify_db"
SQLALCHEMY_DATABASE_URL = "mariadb+pymysql://root:team3@172.17.0.1:3306/tunetalk"

# 데이터베이스 엔진 생성
engine = create_engine(SQLALCHEMY_DATABASE_URL, pool_pre_ping=True)

# 세션 팩토리 및 세션 설정
SessionLocal = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
