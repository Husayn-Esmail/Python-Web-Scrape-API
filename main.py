from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from typing import Optional
from pydantic import BaseModel
import requests

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"),name="static")
templates = Jinja2Templates(directory="templates")

class Data(BaseModel):
    link: str
    text: str
    tag: str


@app.get("/form")
async def form_post(request: Request):
    result= ""
    return templates.TemplateResponse('form.html', context={'request': request, 'result': result})

@app.post("/form")
async def form_post(request: Request, item: Data,  site: str = Form(...), qstring: str = Form(...)):
    item.link = site
    item.text = qstring
    # return templates.TemplateResponse('form.html', context= {"request":request, 'result': result})
    return item

@app.get('/')
def read_root():
    return {"message":"Hello World"}


# @app.post("/scrape/")
# def scrape(item: Item):
#     return item
