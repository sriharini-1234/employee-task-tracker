from database import Base, engine
import models  # Register SQLAlchemy models before creating tables.

if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
    print("Database tables are ready.")
