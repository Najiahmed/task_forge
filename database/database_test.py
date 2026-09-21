from sqlalchemy import text

from database import engine, SessionLocal


def test_connection():
    with engine.connect() as connection:
        result = connection.execute(text("SELECT 1"))
        assert result.scalar_one() == 1


def test_session():
    db = SessionLocal()

    try:
        result = db.execute(text("SELECT 1"))
        assert result.scalar_one() == 1
    finally:
        db.close()