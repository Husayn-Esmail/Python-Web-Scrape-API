from typing import Optional
from fastapi.respones import HTMLResponse
from fastapi import FastAPI, Form
from pydantic import BaseModel
import requests
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"),name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/items/{id}", response_class=HTMLResponse)
async def read_thing(request: Request, id: str):
    return templates.TemplateResponse("form.html", {"request": request, "id": id})

class Item(BaseModel):
    qurl: str
    qstring: str

@app.get('/')
def read_root():
    return {"message":"Hello World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
        return {"item_id": item_id, "q":q}

@app.post("/scrape/")
def scrape(item: Item):
    return item

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}
