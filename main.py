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
import schemas

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
    print("string: " [start_index:end_index+1])
    return html_string[start_index:end_index+1]

# function to store previous queries in the database
def write_to_db(link, string, tag):
    pass

# These two routes serve output and accept input.
# this is supposed to handle form submissions but at the moment is not working
# functionality so far is working with the docs link just not with the form. 
@app.post("/form", response_model=schemas.PrevQuery)
def form_post(
    request: Request,  
    prev_query: schemas.PrevQuery = fastapi.Depends(schemas.PrevQuery.as_form),
    db: _orm.Session=fastapi.Depends(services.get_db)):
    # Empty by default
    result = ""
    # set all entered paramaters as lowercase for consistency when searching/storing in the db
    prev_query.link = prev_query.link.lower()
    prev_query.qstring = prev_query.qstring.lower()
    # note this will always return false while I'm working on the database part. 
    q = services.get_queries_by_link(db=db, link=prev_query.link) # named q for query
    # DEBUG PRINT STATEMENTS
    # print("full query: ", prev_query)
    # print("query: ", q)
    # print("Prevquery.link: ", prev_query.link)
    # print("prevQuery.string: ", prev_query.qstring)
    # handles the case where new 
    if q == []:
        result = find_string(prev_query.link, prev_query.qstring)
        # handles the case where the queried string is not found.
        result = "not found" if result == "" else result
        prev_query.tag = result
        x = services.create_prev_query(db=db, prev_query=prev_query)
    
    # this will return a tag from the database if the query returned a non-empty list
    count = 0
    for que in q:
        if (que.link.lower() == prev_query.link and que.qstring == prev_query.qstring):
            print("grabbed from db")
            result = que.tag
            break
        count += 1
    # This handles the case where link is same but qstring is different (and not in db)
    if (count == len(q)):
        result = find_string(prev_query.link, prev_query.qstring)
        result = "not found" if result == "" else result
        prev_query.tag = result
        x = services.create_prev_query(db=db, prev_query=prev_query)

    # this returns the new value of result to the end user.
    return templates.TemplateResponse('form.html', context= {"request":request, 'result': result})

# this will serve my form template at the specified path
@app.get("/form", response_class=HTMLResponse)
def form_post(request: Request):
    # returns a webpage with a form on it.
    return templates.TemplateResponse('form.html', context={'request': request})


# temporarily commented out
@app.get('/')
def read_root(request:Request):
    return templates.TemplateResponse("landing.html", context={'request':request})
