from pydantic import BaseModel
from fastapi import Form
from typing import Type, Optional
import inspect

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
    tag: Optional[str] = None # optional because it will be added later.


# everything required for the PrevQuery object is required in the base and thus inherited
# the only reason this works with the form is because the name of the form is the same
# as the labels in here. Everything has to be consistent
# note this code is not mine. it's from a stack overflow post which I read but didn't
# manage to get working without this video. He also mentions the stack overflow post
# video link: https://www.youtube.com/watch?v=L4WBFRQB7Lk
class PrevQuery(PrevQueryBase):
    link: str
    qstring: str
    tag: Optional[str] = None

    @classmethod
    def as_form(
        cls,
        link: str = Form(...),
        qstring: str = Form(...),
        tag: Optional[str] = None
    ):
        return cls(
            link = link,
            qstring = qstring,
            tag = tag
        )
