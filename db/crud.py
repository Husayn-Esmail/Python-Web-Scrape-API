from sqlalchemy.orm import Session

from . import models, schemas

def get_prev_query(db: Session, link: str, qstring: str, tag: str):
    return db.query(modles.Prev_Query).filter(models.Prev_Query.link == link and models.Prev_Query.qstring == qstring).first()

