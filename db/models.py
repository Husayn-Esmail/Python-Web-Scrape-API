from sqlalchemy import Boolean, Column, ForeignKey, Integer, string
from sqlalchemy.orm import relationship

from .database import Base
class Prev_Query(Base):
    __tablename__ = "prev_queries"
    link = Column(String)
    qstring = Column(String, unique=True)
    tag = Column(String)

