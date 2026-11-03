import os
from pathlib import Path

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

load_dotenv()


def resolve_database_url():
    configured_url = os.getenv("DATABASE_URL", "").strip()
    if configured_url and "******" not in configured_url:
        return configured_url

    project_root = Path(__file__).resolve().parent
    sqlite_path = project_root / "employee_task_tracker.db"
    return f"sqlite:///{sqlite_path.as_posix()}"


DATABASE_URL = resolve_database_url()
engine = create_engine(DATABASE_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
