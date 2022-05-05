from pydantic import BaseModel
from fastapi import Form
from typing import Type, Optional
import inspect
# from pydantic.fields import ModelField
# the base model is designed like this because the intention is to add to the database
# once the query has been completed (at the end of the process). Therefore all 
# information should be known at the time of adding the query to the database
# and there should be no extra information required. 
# the base model for a previous query
class PrevQueryBase(BaseModel):
    '''
    Link is the url, I didn't want to use url in case it was a reserved keyword.
    qstring is the text that will be searched on the website, string could also be
    a reserved keyword so I decided not to use just string.
    tag is the HTML tag that is associated with qstring, it will either be the only
    occurrence or the last occurence on the site.
    '''
    link: str
    qstring: str

# Everything required to create a previous query comes from the PrevQueryBase class
class PrevQueryCreate(PrevQueryBase):
    link: str
    qstring: str
    tag: Optional[str] = None


# everything required for the PrevQuery object is required in the base and thus inherited
class PrevQuery(PrevQueryBase):
    link: str
    qstring: str
    tag: Optional[str] = None
