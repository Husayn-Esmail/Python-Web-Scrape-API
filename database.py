# database things
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# This selects the database
SQLALCHEMY_DATABASE_URL = "sqlite:///./tagselect.db"

# this creates the database engine
engine = create_engine (
    # it is formatted this way for sqlite 
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread":False}
)
# will be used to create database sessions
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# models will be inherited from Base
Base = declarative_base()