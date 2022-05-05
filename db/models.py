from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base

class PrevQuery(Base):
    # name of the table to use
    __tablename__ = "queries"
    # columns in the database table
    link = Column(String, index=True)
    qstring = Column(String, primary_key=True, index=True)
    tag = Column(String, index=True)

