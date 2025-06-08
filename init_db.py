from sqlalchemy import create_engine
import time
import os

def init_db():
    POSTGRES_USER = os.getenv("POSTGRES_USER", "postgres")
    POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", "postgres")
    POSTGRES_DB = os.getenv("POSTGRES_DB", "fastapi_db")
    POSTGRES_HOST = os.getenv("POSTGRES_HOST", "db")

    # Wait for PostgreSQL to be ready
    for _ in range(30):
        try:
            engine = create_engine(f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}/{POSTGRES_DB}")
            engine.connect()
            print("Database connection successful")
            break
        except Exception as e:
            print(f"Waiting for database... {str(e)}")
            time.sleep(1)
    else:
        raise Exception("Could not connect to database")

    # Import models and create tables
    from models import Base
    Base.metadata.create_all(bind=engine)
    print("Database tables created successfully")

if __name__ == "__main__":
    init_db() 