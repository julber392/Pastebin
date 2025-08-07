import os
import boto3

from fastapi import FastAPI, Request, Form, Depends, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from src import models, schemas, database
from sqlalchemy.orm import Session
from src.config import ACCESS_KEY, SECRET_KEY, BUCKET_NAME
app = FastAPI()


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app.mount("/static", StaticFiles(directory="src/static"), name="static")
templates = Jinja2Templates(directory="src/templates")

s3 = boto3.client(
    's3',
    endpoint_url='https://storage.yandexcloud.net',
    aws_access_key_id=ACCESS_KEY,
    aws_secret_access_key=SECRET_KEY
)
models.Base.metadata.create_all(bind=database.engine)

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
async def index(request: Request):
    return templates.TemplateResponse("form.html", context={"request": request})

@app.post("/upload")
async def upload(request: Request, text_content: str = Form(...),db: Session = Depends(get_db)):
    new_data = models.User(data=text_content, hashed_data="123")
    db.add(new_data)
    db.commit()
    db.refresh(new_data)

    s3.put_object(
        Bucket=BUCKET_NAME,
        Key="Something.txt",
        Body=text_content.encode('utf-8')
    )
    return templates.TemplateResponse("link.html", context={"request": request})