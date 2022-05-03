from sqlalchemy.orm import Session

from . import models, schemas

def get_prev_query(db: Session, link: str, qstring: str, tag: str):
    return db.query(modles.Prev_Query).filter(models.Prev_Query.link == models.Prev_Query.qstring == qstring).first()

def get_query_by_url(db: Session, link: str):
    return db.query(models.Prev_Query).filter(models.Prev_Query.link == link).first()

def get_prev_queries(db: Session, skip: int=0, limit: int =100):
    return db.query(models.Prev_Query).offset(skip).limit(limit).all()

def create_prev_query(db: Session, query: schemas.Prev_Query_Create):
    db_prev_query = models.Prev_Query(link=Prev_Query.link, qstring = Prev_Query.qstring, tag = Prev_Query.tag)
    db.add(db_prev_query)
    db.commit()
    db.refresh(db_prev_query)
    return db_prev_query