from pydantic import BaseModel

# the base model for a previous query
class PrevQueryBase(BaseModel):
    '''
    Link is the url, I didn't want to use url in case it was a reserved keyword.
    qstring is the text that will be searched on the website, string could also be
    a reserved keyword so I decided not to use just string.
    tag is the HTML tag that is associated with qstring, it will either be the only
    occurrence or the last occurence on the site, it could also be empty if the
    qstring doesn't exist on the site but that's an edge case I haven't figured
    out how to handle as of writing this docstring on May 3. I do expect to have
    it completed by the duedate.
    '''
    link: str
    qstring: str
    tag: str

# Everything required to create a previous query comes from the PrevQueryBase class
class PrevQueryCreate(PrevQueryBase):
    pass

# everything required for the PrevQuery object is required in the base and thus inherited
class PrevQuery(PrevQueryBase):
    pass