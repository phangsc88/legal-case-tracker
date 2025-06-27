import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Try the env var first; otherwise use a hard-coded local connection
DATABASE_URL = os.environ.get(
    "DATABASE_URL",
    "postgresql+psycopg2://legal_app_user:1234@localhost:5432/legal_tracker"
)

engine = create_engine(DATABASE_URL, echo=False)
SessionLocal = sessionmaker(bind=engine)

def get_db_connection():
    """Returns a new SQLAlchemy Connection."""
    return engine.connect()
