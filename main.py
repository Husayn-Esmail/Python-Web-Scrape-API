# fast api things
from fastapi import FastAPI, Form, Request, Depends, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
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


# function to query database
def query_db(link, string):
    return False

# function to search for the given string, returns the html element (string)
def find_string(link, string):
    # preliminary work
    html_string = requests.get(link).text
    # start the search
    occurence_index = html_string.lower().rfind(string)
    start_index = occurence_index
    end_index = occurence_index
    start = html_string[start_index]
    end = html_string[end_index]
    # finding the full element
    while (start != "<"):
        start_index -= 1
        start = html_string[start_index]
    while (end != ">"):
        end_index += 1
        end = html_string[end_index]
    return html_string[start_index:end_index+1]

# function to store previous queries in the database
def write_to_db(link, string, tag):
    pass

class creatquery():
    def __init__(self, site, qstring, result):
        self.site = site
        self.qstring = qstring
        self.result = result


# These two routes serve output and accept input.
# this is supposed to handle form submissions but at the moment is not working
@app.post("/form")
async def form_post(request: Request,  site: str = Form(...), qstring: str = Form(...)):
    # Empty by default
    result = ""
    # note this will always return false while I'm working on the database part. 
    in_db = query_db(site, qstring)
    if (not in_db):
        result = find_string(site, qstring)
    # handles the case where the queried string is not found.
    result = "Not found" if result == "" else result
    # prev_query = creatquery(site, qstring, result)
    # crud.createPrevQuery(get_db(), prev_query)

    # somewhere in this void, the database needs to be accessed and needs to write the result of the query. 


    # this returns the new value of result to the end user.
    return templates.TemplateResponse('form.html', context= {"request":request, 'result': result})

# this will serve my form template at the specified path
@app.get("/form", response_class=HTMLResponse)
def form_post(request: Request):
    # returns a webpage with a form on it.
    return templates.TemplateResponse('form.html', context={'request': request})


# serves a page at the root directory. doesn't do anything right now
@app.get('/')
def read_root(request:Request):
    return templates.TemplateResponse("landing.html", context={'request':request})
