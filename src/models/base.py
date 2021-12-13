from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine

from src.config import DATABASE_URI

# create an engine
engine = create_engine('postgresql://arcane_user:arcane_pass@localhost:5432/arcane')

# create a configured "Session" class
Session = sessionmaker(bind=engine)

# create a Session
session = Session()

# declarative base class
Base = declarative_base()

 

