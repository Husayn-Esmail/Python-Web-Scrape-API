# fast api things
from fastapi import FastAPI, Form, Request, Depends, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from typing import Optional
from pydantic import BaseModel
# requests for handling get and post
import requests


from db import crud, models, schemas
from db.database import engine

models.Base.metadata.create_all(bind=engine)


# this is handling the static files (like css)
app = FastAPI()
app.mount("/static", StaticFiles(directory="static"),name="static")
# this tells fastapi where to find templates
templates = Jinja2Templates(directory="templates")

# this is an object representing what I want to store in the database
class Data(BaseModel):
    link: str
    text: str
    tag: str

# this will serve my form template at the specified path
@app.get("/form")
async def form_post(request: Request):
    result= ""
    return templates.TemplateResponse('form.html', context={'request': request, 'result': result})

# this is supposed to handle form submissions but at the moment is not working
@app.post("/form")
async def form_post(request: Request, item: Data,  site: str = Form(...), qstring: str = Form(...)):
    item.link = site
    item.text = qstring
    return templates.TemplateResponse('form.html', context= {"request":request, 'result': result})
    # return item

# serves a page at the root directory. doesn't do anything right now
@app.get('/')
def read_root():
    return {"message":"Hello World"}


# @app.post("/scrape/")
# def scrape(item: Item):
#     return item
