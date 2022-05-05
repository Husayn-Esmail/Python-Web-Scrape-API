# fast api things
from fastapi import FastAPI, Request, Form, HTTPException
import fastapi
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
# requests for handling get and post
import requests
import sqlalchemy.orm as _orm
import services
import schemas, models

# this is handling the static files (like css)

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"),name="static")
# this tells fastapi where to find templates
templates = Jinja2Templates(directory="templates")
# create the database
services.create_database()

# function to search for the given string, returns the html element (string)
def find_string(link, string):
    # preliminary work
    html_string = requests.get(link).text
    # start the search
    occurence_index = html_string.lower().rfind(string.lower())
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
    print("string: " [start_index:end_index+1])
    return html_string[start_index:end_index+1]

# function to store previous queries in the database
def write_to_db(link, string, tag):
    pass

# These two routes serve output and accept input.
# this is supposed to handle form submissions but at the moment is not working
@app.post("/form", response_model=schemas.PrevQuery)
def form_post(
    request: Request,  
    prev_query: schemas.PrevQuery,
    db: _orm.Session=fastapi.Depends(services.get_db)):
    # Empty by default
    result = ""
    # note this will always return false while I'm working on the database part. 
    q = services.get_queries_by_link(db=db, link=prev_query.link) # named q for query
    print("full query: ", prev_query)
    print("query: ", q)
    print("Prevquery.link: ", prev_query.link)
    print("prevQuery.string: ", prev_query.qstring)
    if q == []:
        result = find_string(prev_query.link, prev_query.qstring)
        # handles the case where the queried string is not found.
        result = "Not found" if result == "" else result
        prev_query.tag = result
        x = services.create_prev_query(db=db, prev_query=prev_query)
    

    # somewhere in this void, the database needs to be accessed and needs to write the result of the query. 


    # this returns the new value of result to the end user.
    return templates.TemplateResponse('form.html', context= {"request":request, 'result': result})

# this will serve my form template at the specified path
@app.get("/form", response_class=HTMLResponse)
def form_post(request: Request):
    # returns a webpage with a form on it.
    return templates.TemplateResponse('form.html', context={'request': request})


# temporariliy commented out
# @app.get('/')
# def read_root(request:Request):
#     return templates.TemplateResponse("landing.html", context={'request':request})
