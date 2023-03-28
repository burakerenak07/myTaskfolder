from fastapi import FastAPI, BackgroundTasks, HTTPException,Path
from pydantic import BaseModel
from extract import getIt
from typing import Optional, List
from typing import Optional
from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from langdetect import detect

app = FastAPI()
inventory={}

class Item(BaseModel):
    myLink: str


@app.post("/process_link")
async def process_link(link: str = Form(...)):
    exec=getIt(link)
    inventory[0]=exec
    return inventory[0]

@app.get("/", response_class=HTMLResponse)
async def show_form(request: Request):
    return """
        <html>
            <head>
                <title>Get link and process</title>
            </head>
            <body>
                <form method="post" action="/process_link">
                    <input type="text" name="link">
                    <button type="submit">Process link</button>
                </form>
            </body>
        </html>
    """
 