from dotenv import load_dotenv
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
load_dotenv(os.path.join(BASE_DIR, ".env"))

ACCESS_KEY = os.getenv("ACCESS_KEY")
SECRET_KEY = os.getenv("SECRET_KEY")
BUCKET_NAME = os.getenv("BUCKET_NAME")
DEBUG = os.getenv("DEBUG") == "True"
SQLALCHEMY_DATABASE_URL = os.getenv("SQLALCHEMY_DATABASE_URL")

if not (SQLALCHEMY_DATABASE_URL and ACCESS_KEY and SECRET_KEY\
        and BUCKET_NAME):
    raise ValueError("Переменные не найдены в .env")
