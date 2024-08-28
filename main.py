from fastapi import FastAPI
from pydantic import BaseModel
from app import app_router

app = FastAPI()

app.include_router(router=app_router, prefix="/api")

class Login(BaseModel):
    username: str
    password: str

@app.get("/")
async def root():
    return "homepage"

@app.post("/login")
async def login(data: Login):
    print(data)
    return "login credentials received"


