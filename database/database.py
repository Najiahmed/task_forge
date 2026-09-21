from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from sqlalchemy import text

DATABASE_URL = (
    "postgresql://postgres.blwooevevzgqudbtwjer:Bicyclette.340@aws-1-eu-west-1.pooler.supabase.com:5432/postgres"
)

engine= create_engine(DATABASE_URL)

SessionLocal = sessionmaker(engine)

class Base(DeclarativeBase):
    pass


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

