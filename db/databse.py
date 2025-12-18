from sqlalchemy import String, Integer, create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker


engine = create_engine("sqlite:///./db.sqlite", connect_args="check_same_thread")
SessionLocal = sessionmaker(autoflush=False, authcommit=False, bind=engine)

class Base(DeclarativeBase):
    pass


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close