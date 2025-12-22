from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,DeclarativeBase
import os
from dotenv import load_dotenv

load_dotenv()

# DB_HOST = os.getenv("DB_HOST")
# DB_PORT = os.getenv("DB_PORT")
# DB_USER = os.getenv("DB_USER")
# DB_PASSWORD = os.getenv("DB_PASSWORD")
# DB_NAME = os.getenv("DB_NAME")

# DATABASE_URL = (
#   F"mysql+pymysql://{DB_USER}:{DB_PASSWORD}"
#   f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
# )

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine (
  DATABASE_URL,
  pool_pre_ping = True,
  pool_recycle = 500
)

SessionLocal = sessionmaker(
  autoflush= False,
  autocommit = False,
  bind = engine
)

class Base(DeclarativeBase):
    pass

def get_db():
  db = SessionLocal()
  try:
    yield db
  finally:
    db.close()
