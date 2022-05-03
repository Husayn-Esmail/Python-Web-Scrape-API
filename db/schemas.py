from typing import List, Optional
from pydantic import BaseModel


# not sure if these classes are all needed, just following a tutorial.
# I'll reduce as things work out more. 
class Prev_Query_Base(BaseModel):
    link: str
    qstring: str
    tag: str

class Prev_Query_Create(Prev_Query_Base):
    pass


class Prev_Query(Prev_Query_Base):
    link: str
    qstring: str
    tag: str