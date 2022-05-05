from sqlalchemy.orm import Session
import models, schemas

# this should get the whole PrevQuery object, or at least the minimum information
# to identify a query.
def getPrevQuery(db: Session, link: str, qstring: str, tag: str):
    return db.query(models.PrevQuery).filter(models.PrevQuery.link == models.PrevQuery.qstring == qstring).first()

# this should allow you to narrow down a query by url so that you can check qstring
def getQueryByURL(db: Session, link: str):
    return db.query(models.PrevQuery).filter(models.PrevQuery.link == link).first()

# this will get a certain amount of queries I think.
# to be completely honest at this moment, I don't know exactly what
# these blocks of code are doing.
def getPrevQueries(db: Session, skip: int=0, limit: int =100):
    return db.query(models.PrevQuery).offset(skip).limit(limit).all()

# this should allow us to add previous queries to the database. 
def createPrevQuery(db: Session, query: schemas.PrevQueryCreate):
    # builds the structure to add to database
    dbPrevQuery = models.PrevQuery(link=PrevQuery.link, qstring = PrevQuery.qstring, tag = PrevQuery.tag)
    db.add(dbPrevQuery) # adds structure to database
    db.commit() # commits the change
    db.refresh(dbPrevQuery) # refreshes the database I think? 
    return dbPrevQuery # returns the structure. 