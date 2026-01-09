import os

from fastapi import FastAPI
import uvicorn
from dotenv import load_dotenv

load_dotenv(dotenv_path='../.env')
HOST = os.getenv('HOST', '0.0.0.0')
PORT = os.getenv('PORT', 8000)
RELOAD = os.getenv('RELOAD', True)

app = FastAPI()


if __name__ == "__main__":
    uvicorn.run("main:app", host=HOST, port=PORT, reload=RELOAD)
