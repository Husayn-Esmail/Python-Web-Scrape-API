import sqlalchemy.orm as _orm
import crud, models, schemas
from database import engine
import database

def create_database():
    return models.Base.metadata.create_all(bind=engine)

# dependency
def get_db():
    # create the database session
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


# crud functionality is in this code
# gets all queries with the same qstring
def get_queries_by_qstring(db: _orm.Session, qstring: str):
    return db.query(models.PrevQuery).filter(models.PrevQuery.qstring == qstring)

# gets all queries with the same link
def get_queries_by_link(db: _orm.Session, link: str):
    return db.query(models.PrevQuery).filter(models.PrevQuery.link == link).all()

# this is supposed to get the tag based on link and qstring
def get_tag(db: _orm.Session, link: str, qstring: str):
    return db.query(models.PrevQuery).filter(models.PrevQuery.tag).first()

# adds a previous query to the database
def create_prev_query(db: _orm.Session, prev_query: schemas.PrevQueryCreate):
    db_query = models.PrevQuery(link=prev_query.link, qstring=prev_query.qstring, tag=prev_query.tag)
    db.add(db_query)
    db.commit()
    db.refresh(db_query)
    return db_query