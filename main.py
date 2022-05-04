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

# dependency
def get_db():
    # this allows main to access database 
    # this should allow me to connect front end to database.
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# this is handling the static files (like css)
app = FastAPI()
app.mount("/static", StaticFiles(directory="static"),name="static")
# this tells fastapi where to find templates
templates = Jinja2Templates(directory="templates")

# this is supposed to handle form submissions but at the moment is not working
@app.post("/form")
async def form_post(request: Request,  site: str = Form(...), qstring: str = Form(...)):
    result = site+qstring
    print(result)
    return templates.TemplateResponse('form.html', context= {"request":request, 'result': result})

# this will serve my form template at the specified path
@app.get("/form", response_class=HTMLResponse)
def form_post(request: Request):
    return templates.TemplateResponse('form.html', context={'request': request})


# serves a page at the root directory. doesn't do anything right now
@app.get('/')
def read_root():
    return {"message":"Hello World"}
