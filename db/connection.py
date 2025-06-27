import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
DATABASE_URL = os.environ["DATABASE_URL"]
engine = create_engine(DATABASE_URL, echo=False)
SessionLocal = sessionmaker(bind=engine)
def get_db_connection():
return engine.connect()
