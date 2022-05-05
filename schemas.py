from pydantic import BaseModel
from fastapi import Form
from typing import Type
import inspect
from pydantic.fields import ModelField
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
    pass


# def as_form(cls: Type[BaseModel]):
#     """
#     Adds an as_form class method to decorated models. The as_form class method
#     can be used wtih FastAPI endpoints
#     """
#     new_params = [
#         inspect.Parameter(
#             field.alias,
#             inspect.Parameter.POSITIONAL_ONLY,
#             default=(Form(field.default) if not field.required else Form(...)),
#             annotation=field.outer_type_,
#         )
#         for field in cls.__fields__.values()
#     ]
#     async def _as_form(**data):
#         return cls(**data)

#     sig = inspect.signature(_as_form)
#     sig = sig.replace(parameters=new_params)
#     as_form._signature__ = sig
#     setattr(cls, "as_form", _as_form)
#     return cls

# def as_form(cls: Type[BaseModel]):
#     new_parameters = []

#     for field_name, model_field in cls.__fields__.items():
#         model_field: ModelField  # type: ignore

#         if not model_field.required:
#             new_parameters.append(
#                 inspect.Parameter(
#                     model_field.alias,
#                     inspect.Parameter.POSITIONAL_ONLY,
#                     default=Form(model_field.default),
#                     annotation=model_field.outer_type_,
#                 )
#             )
#         else:
#             new_parameters.append(
#                 inspect.Parameter(
#                     model_field.alias,
#                     inspect.Parameter.POSITIONAL_ONLY,
#                     default=Form(...),
#                     annotation=model_field.outer_type_,
#                 )
#             )

#     async def as_form_func(**data):
#         return cls(**data)

#     sig = inspect.signature(as_form_func)
#     sig = sig.replace(parameters=new_parameters)
#     as_form_func.__signature__ = sig  # type: ignore
#     setattr(cls, 'as_form', as_form_func)
#     return cls



# everything required for the PrevQuery object is required in the base and thus inherited
class PrevQuery(PrevQueryBase):
    link: str
    qstring: str
    tag: str

    # @classmethod
    # def as_form(
    #     cls,
    #     link: str = Form(...),
    #     qstring: str = Form(...)
    # ) -> PrevQuery:
    #     return cls(link=link, qstring=qstring)